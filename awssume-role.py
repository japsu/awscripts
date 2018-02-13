#!/usr/bin/env python3

import os
import configparser
import sys
import uuid

import boto3


def main(token_code, serial_number, role_arn):
    role_session_name = f'awssume-role-{uuid.uuid4()}'

    sts = boto3.client('sts')
    response = sts.assume_role(
        RoleArn=role_arn,
        RoleSessionName=role_session_name,
        SerialNumber=serial_number,
        TokenCode=token_code,
    )

    access_key_id = response['Credentials']['AccessKeyId']
    secret_access_key = response['Credentials']['SecretAccessKey']
    session_token = response['Credentials']['SessionToken']

    print(f'export AWS_ACCESS_KEY_ID={access_key_id}')
    print(f'export AWS_SECRET_ACCESS_KEY={secret_access_key}')
    print(f'export AWS_SESSION_TOKEN={session_token}')


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read(os.path.expanduser('~/.aws/config'))

    unused, profile_name, token_code = sys.argv

    serial_number = config.get(f'profile {profile_name}', 'mfa_serial')
    role_arn = config.get(f'profile {profile_name}', 'role_arn')

    main(token_code, serial_number, role_arn)

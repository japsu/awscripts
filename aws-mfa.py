#!/usr/bin/env python3

import os
import configparser
import sys

import boto3


def main(token_code, serial_number):
    sts = boto3.client('sts')
    response = sts.get_session_token(
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
    config.read(os.path.expanduser('~/.aws/credentials'))

    serial_number = config.get('default', 'mfa_serial')
    token_code = sys.argv[1]

    main(token_code, serial_number)

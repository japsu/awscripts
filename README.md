# Useful scripts for the AWS CLI

## Installation

    pip3 install boto3
    install -m 755 ./awssume-role.py /usr/local/bin/awssume-role

## Configuration

### `~/.aws/config`

A profile with `role_arn` and `mfa_serial` is required for `awssume-role`.

    [default]
    region = eu-central-1

    [profile prod]
    role_arn = arn:aws:iam::…
    source_profile = default
    mfa_serial = arn:aws:iam::…

### `~/.aws/credentials`

Put your `aws_access_key_id` and `aws_secret_access_key` here:

    [default]
    aws_access_key_id = …
    aws_secret_access_key = …

## Usage

### `eval $(awssume-role prod 666666)`

If you need MFA to be able to role switch.

Uses the STS *assume_role* API to get a session token using the provided role ARN and MFA token.

### Command output

If you run the above command without `eval $(…)`, you'll notice they output `export` statements such as this:

    export AWS_ACCESS_KEY_ID=…
    export AWS_SECRET_ACCESS_KEY=…
    export AWS_SESSION_TOKEN=…

## License

    Copyright © 2018 Santtu Pajukanta

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

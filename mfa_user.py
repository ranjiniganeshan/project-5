import boto3
from botocore.exceptions import ClientError

# Initialize a session using IAM
iam_client = boto3.client('iam')

def list_all_users():
    try:
        # List all IAM users in the account
        paginator = iam_client.get_paginator('list_users')
        for response in paginator.paginate():
            for user in response['Users']:
                yield user['UserName']
    except ClientError as e:
        print(f"Error listing users: {e}")

def check_mfa_enabled_for_all_users():
    try:
        # Iterate through all IAM users
        for user_name in list_all_users():
            # List MFA devices for each user
            response = iam_client.list_mfa_devices(UserName=user_name)

            # Check if any MFA devices are associated with the user
            if response['MFADevices']:
                print(f"MFA is enabled for user {user_name}.")
                for device in response['MFADevices']:
                    print(f"  - Device Serial Number: {device['SerialNumber']}")
            else:
                print(f"MFA is not enabled for user {user_name}.")

    except ClientError as e:
        print(f"An error occurred: {e}")

# Run the function to check MFA for all users
check_mfa_enabled_for_all_users()

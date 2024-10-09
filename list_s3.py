import boto3

# Initialize a session using Amazon S3
s3_client = boto3.client('s3')

# List all S3 buckets
response = s3_client.list_buckets()

# Output bucket names
for bucket in response['Buckets']:
    print(bucket["Name"])

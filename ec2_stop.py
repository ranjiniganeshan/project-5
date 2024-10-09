import boto3
 

region = "us-west-2"
ec2client = boto3.client('ec2',region_name=region)
 
all_instances = ec2client.describe_instances(Filters=[{'Name':'tag:Name','Values':["docker"]}
                                                      ])
for reservation in all_instances['Reservations']:
    for instance in reservation['Instances']:
        instance_ids = instance['InstanceId']
        print("Stopping Instances {}".format(instance_ids))
        ec2client.stop_instances(InstanceIds=[instance_ids])
 

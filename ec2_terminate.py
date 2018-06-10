import boto3
client = boto3.client('ec2')
response = client.terminate_instances(
    InstanceIds=[
        'i-0a42ecce8fd3cc086',
    ],
    DryRun=False
)

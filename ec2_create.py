import boto3
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-922914f7',
    InstanceType='t2.micro',
    KeyName='first',
    MaxCount=1,
    MinCount=1,
   SecurityGroupIds=[
        'sg-018439b794ac8f0b8'
    ]
    )
print instance

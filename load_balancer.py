import boto3
client = boto3.client('elb')
response = client.create_load_balancer(
    Listeners=[
        {
            'InstancePort': 80,
            'InstanceProtocol': 'HTTP',
            'LoadBalancerPort': 80,
            'Protocol': 'HTTP',
        },
    ],
    LoadBalancerName='my-load-balancer',
    SecurityGroups=[
        'sg-018439b794ac8f0b8',
    ],
    Subnets=[
        'subnet-70c5cb3d',
        'subnet-7e88e916',
        'subnet-db73ada1'

    ],
)

print(response['DNSName'])

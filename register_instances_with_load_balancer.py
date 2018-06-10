import boto3
client = boto3.client('elb')
response = client.register_instances_with_load_balancer(
    LoadBalancerName='my-load-balancer',
    Instances=[
        {
            'InstanceId': 'i-0dde574774ebb4d87'
        },
 	{
            'InstanceId': 'i-02215d80b070dbfc9'
        }
    ]
)

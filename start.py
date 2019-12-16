import json
import datetime
import boto3

region = 'us-east-1'

instances = ['i-0f41e6157d37ec40e']

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)

    data = {
        'output': 'start instances'+ str(instances),
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}

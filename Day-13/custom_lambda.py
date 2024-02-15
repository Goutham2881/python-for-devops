import boto3
import time
def lambda_handler(event, context): 
    stopped_ec2s= []
    client = boto3.client('ec2')
    responses = client.describe_instances(
        Filters = [
            {'Name': 'instance-state-name', 
             'Values' : ['stopped']
             }
        ]
    )
    responses_list= responses['Reservations']
    
    for response in responses_list:
        stopped_ec2s.append(response['Instances'][0]['InstanceId'])
    
    print(stopped_ec2s)
    
    client.terminate_instances(
            InstanceIds=stopped_ec2s
        )
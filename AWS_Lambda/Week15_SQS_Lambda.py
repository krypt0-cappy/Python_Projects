import json
import boto3

from datetime import datetime

def lambda_handler(event, context):
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    
    sqs = boto3.client('sqs')
    
    sqs.send_message(QueueUrl="https://queue.amazonaws.com/741179323687/Week15Project-current-time", MessageBody=date_time)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Congratulations! You have successfully Executed the function. You are a rock star!')
    }
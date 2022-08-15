import boto3


sqs_message = boto3.resource('sqs')


sqs_queue = sqs_message.create_queue(QueueName='current-time')

print(sqs_queue.url)


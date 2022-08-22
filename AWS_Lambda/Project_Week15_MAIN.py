import boto3

# Get the sqs service resource
sqs = boto3.resource('sqs')

# Create the queue. Add a delay of 3 seconds. Creates and returns the queue instance
sqs_queue = sqs.create_queue(QueueName='Week15Project-current-time', Attributes={'DelaySeconds': '3'})

# Prints the sqs url and the attribute delay
print(sqs_queue.url)
print(sqs_queue.attributes.get('DelaySeconds'))
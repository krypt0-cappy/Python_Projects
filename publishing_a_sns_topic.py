import boto3

def sns_publish_topic(sns_client, TopicArn, Message):
    sns_client.publish(TopicArn=TopicArn, Message=Message)


if __name__ == "__main__":
    sns = boto3.client('sns')
    sns_publish_topic(sns, 'arn:aws:sns:us-east-1:741179323687:Avengers_Rules', "Proof Tony Stark does have a heart!!!!")
    
    
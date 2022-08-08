import json
import boto3


ec2 = boto3.resource('ec2', region_name='us-east-1')

def start_stopped_instances(ec2):
    stopped_instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']},{'Name': 'tag:Env','Values':['Dev']}])
    for instance in stopped_instances:
        id=instance.id
        ec2.instances.filter(InstanceIds=[id]).start()
print("All Environment:Dev Instances are now started.")
    
if __name__ == "__main__":
    start_stopped_instances(ec2)
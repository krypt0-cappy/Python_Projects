import json
import boto3


ec2 = boto3.resource('ec2', region_name='us-east-1')

def stop_running_instances(ec2):
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
        id=instance.id
        if("i-06f1af0ebcd74388b" != id):
            ec2.instances.filter(InstanceIds=[id]).stop()
print("All Instances are now stopped.")
    
if __name__ == "__main__":
    stop_running_instances(ec2)

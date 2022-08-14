import boto3


# How to create an EC2 Instance using Boto3

ec2_instance = boto3.client('s3')

response = ec2_instance.run_instances(
    ImageId='ami-090fa75af13c156b4',
    InstanceType='t2.micro',
    KeyName='boto3_test_keypair',
    MinCount=1,
    MaxCount=1
    )
    
print("You have successfully created a new EC2 Instance using BOTO3!")
import os
import sys
sys.path.append('../')

from list_instance_ids_boto3 import *

ec2 = boto3.client('ec2')
list_instance_ids(ec2)

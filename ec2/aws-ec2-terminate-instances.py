import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

newlist=[]

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
            newlist.append(instance['InstanceId'])

print(newlist)
print(ec2.terminate_instances(InstanceIds=(newlist)))
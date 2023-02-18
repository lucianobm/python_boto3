import boto3

ec2 = boto3.client('ec2')

response = ec2.create_snapshot(
    Description='snapshot test',
    VolumeId='vol-06d74c26eaccc9f5c'
    )
    
print(response)
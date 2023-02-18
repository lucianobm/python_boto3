import boto3

ec2 = boto3.client('ec2')

response = ec2.create_volume(
    AvailabilityZone='us-east-1d',
    Encrypted=True,
    Size=10,
    SnapshotId='snap-0dfb58fc8218bc849',
    VolumeType='gp2'
    )
    
print(response)
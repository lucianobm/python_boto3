import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_snapshots(
    SnapshotIds=['snap-07ae0b3c8331e0af6']
    )
    
print(response)
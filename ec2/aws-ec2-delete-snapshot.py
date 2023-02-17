import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_snapshot(
    SnapshotId='snap-0dfb58fc8218bc849'
    )
    
print(response)
import boto3

vpc = boto3.client("ec2")

response = vpc.delete_vpc(
    VpcId='vpc-0ed05e681aec9a840'
    )

print(response)
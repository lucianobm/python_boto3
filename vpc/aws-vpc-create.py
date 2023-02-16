import boto3

vpc = boto3.client("ec2")

response = vpc.create_vpc(
    CidrBlock='10.255.0.0/24'
    )

print(response)
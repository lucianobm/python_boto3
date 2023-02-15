import boto3

s3 = boto3.client('s3')

bucket_name = "testbucket7893467"

s3.delete_object(
    Bucket=bucket_name,
    Key='upload1.png'
    )
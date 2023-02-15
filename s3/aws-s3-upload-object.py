import boto3

s3 = boto3.client('s3')

s3.upload_file(
    Filename="uploadteste.png",
    Bucket="testbucket7893467",
    Key="uploadtest.png")
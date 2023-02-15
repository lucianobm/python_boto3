import boto3

s3 = boto3.client('s3')

bucket_name = "testbucket7893467"

response = s3.list_objects(Bucket=bucket_name)

contents = response["Contents"]

for content in contents:
    response=s3.delete_object(Bucket=bucket_name,Key=content['Key'])
    print(response)
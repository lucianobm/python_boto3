import boto3

#aws_resource = boto3.resource('s3')
#bucket = aws_resource.Bucket('testbucket789346')

s3 = boto3.resource('s3')
bucket = s3.Bucket('testbucket7893467')

response = bucket.create(
#    ACL='public-read'
    ACL='private'
#    CreateBucketConfiguration={
#        'LocationConstraint':'us-east-1'
#    },
)

print(response)
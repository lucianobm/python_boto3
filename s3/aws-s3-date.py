import boto3

s3 = boto3.client('s3')

#print(s3.list_buckets())
#print(s3.list_buckets()["Buckets"])
#print(s3.list_buckets()["Buckets"][0])
#print(s3.list_buckets()["Buckets"][0]["Name"])
#print(s3.list_buckets()["Buckets"][0]["CreationDate"])

creation_date = s3.list_buckets()["Buckets"][0]["CreationDate"]
print(creation_date)

print(creation_date.strftime("%d%m%y_%H:%M:%s"))

for bucket in s3.list_buckets()["Buckets"]:
    #print(bucket)
    #print(bucket["Name"])
    #print(bucket["CreationDate"])
    print(bucket["Name"], bucket["CreationDate"])
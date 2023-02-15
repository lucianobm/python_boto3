import boto3
import os
import glob

cwd = os.getcwd()
cwd = cwd+"/upload"
print(cwd)

files = glob.glob(cwd+"*.png")
print(files)

for file in files:
    s3 = boto3.client('s3')
    s3.upload_file(
    Filename=file,
    Bucket="testbucket7893467",
    Key=file.split("/")[-1])

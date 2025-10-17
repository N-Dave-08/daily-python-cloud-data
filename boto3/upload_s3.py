import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
bucket_name = 'boto3-wrong-bucket'  

try:
    s3.upload_file('hello.txt', bucket_name, 'hello.txt')
    print("Upload Successful!")
except Exception as e:
    print("Upload failed:", e)


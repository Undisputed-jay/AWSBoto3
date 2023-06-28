import boto3
import json

data = json.dumps('marriage.xls')

client = boto3.client('s3')

response = client.put_object(
    Body = data,
    Bucket = 'learning-class-work',
    Key =  'marriage.json'
)


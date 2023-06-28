import boto3

client = boto3.client('s3')

response = client.get_object(
    Bucket = 'learning-class-work',
    Key = 'marriage.xls'
)

print(response)
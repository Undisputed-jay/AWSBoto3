import boto3

client = boto3.client('s3')

delete_bucket = client.delete_bucket(
    Bucket = "learning-class-work"
)
import boto3

s3 = boto3.resource('s3')

create_bucket = s3.create_bucket(
    Bucket = 'learning-class-work',
    CreateBucketConfiguration={
        "LocationConstraint":'eu-west-2'
    }
)

print(create_bucket)
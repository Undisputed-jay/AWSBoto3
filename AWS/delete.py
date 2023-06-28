import boto3

s3 = boto3.resource('s3')

delete_file = s3.Object("learning-class-work", 'rootkey.csv').delete()

print(delete_file)
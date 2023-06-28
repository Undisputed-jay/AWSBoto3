import boto3

s3 = boto3.resource('s3')

upload = s3.Bucket('learning-class-work').upload_file('marriage.xls', 'marriage.xls')

print(upload)

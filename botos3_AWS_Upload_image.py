import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)


data = open('winskull.jpg', 'rb')
s3.Bucket('aonapps').put_object(Key='test/win.jpg', Body=data)
print("done")

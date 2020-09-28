import tinys3

S3_ACCESS_KEY = "YOUR AWS S3_ACCESS_KEY"
S3_SECRET_KEY = "YOUR AWS S3_SECRET_KEY"

conn = tinys3.Connection(S3_ACCESS_KEY, S3_SECRET_KEY)
print("connected")
# print("uploading")

# f = open('winskull.jpg','rb')
# conn.upload('test/win.jpg',f,'aonapps')
# print("DONE")

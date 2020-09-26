import tinys3

S3_ACCESS_KEY = "AKIAJV2SP7VQE44ZGJVA"
S3_SECRET_KEY = "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"

conn = tinys3.Connection(S3_ACCESS_KEY, S3_SECRET_KEY)
print("connected")
# print("uploading")

# f = open('winskull.jpg','rb')
# conn.upload('test/win.jpg',f,'aonapps')
# print("DONE")

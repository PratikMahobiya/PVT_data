# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'YOUR SID'
auth_token = 'YOUR TOKEN'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello,\n This is Trail sms from Pratik Mahobiya\n to check the working of Program.\n\n Thank You",
                     from_='+19046377572',
                     #media_url=['https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg'],
                     to='+91xxxxxxxxxx'
                 )

print(message.sid)
print("sent")

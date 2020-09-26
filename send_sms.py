# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACfa44115d0ff5f4602437ca7a4130b110'
auth_token = 'e054d9870d54ba655fa932e3ffabb83d'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello,\n This is Trail sms from Pratik Mahobiya\n to check the working of Program.\n\n Thank You",
                     from_='+19046377572',
                     #media_url=['https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg'],
                     to='+917000681073'
                 )

print(message.sid)
print("sent")
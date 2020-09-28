# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'YOUR SID'
auth_token = 'YOUR TOKEN'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Someone is detected",
                     media_url=['http://s3-ap-southeast-1.amazonaws.com/aonapps/test/image.jpg'],
                     from_='whatsapp:+14155238886',
                     to='whatsapp:+91xxxxxxxxxx'
                 )

# message = client.messages.create(
#                               from_='whatsapp:+14155238886',
#                               body='Hello, there!',
#                               to='whatsapp:+91xxxxxxxxxx'
#                           )

print(message.sid)

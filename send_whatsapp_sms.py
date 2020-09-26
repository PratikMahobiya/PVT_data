# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACfa44115d0ff5f4602437ca7a4130b110'
auth_token = 'e054d9870d54ba655fa932e3ffabb83d'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Someone is detected",
                     media_url=['http://s3-ap-southeast-1.amazonaws.com/aonapps/test/image.jpg'],
                     from_='whatsapp:+14155238886',
                     to='whatsapp:+917000681073'
                 )

# message = client.messages.create(
#                               from_='whatsapp:+14155238886',
#                               body='Hello, there!',
#                               to='whatsapp:+917000681073'
#                           )

print(message.sid)

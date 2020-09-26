# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACfa44115d0ff5f4602437ca7a4130b110'
auth_token = 'e054d9870d54ba655fa932e3ffabb83d'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+919893578798',
                        from_='+19046377572'
                    )

print(call.sid)

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

with open('C:/Users/Mark/desktop/twilAuth.txt', 'r') as f:
    account_sid = f.readline()
    auth_token = f.readline()
    twil = f.readline()
    me = f.readline()

# Your Account Sid and Auth Token from twilio.com/console
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="Hello, World. This is Mark.",
                    from_=twil,
                    to=me
                )

print(message.sid)

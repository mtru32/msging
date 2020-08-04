# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
    
with open('C:/Users/Mark/desktop/twilAuth.txt', 'r') as f:
    account_sid = f.readline()
    auth_token = f.readline()

# Your Account Sid and Auth Token from twilio.com/console
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+18139061773',
                     to='+16082129272'
                 )

print(message.sid)
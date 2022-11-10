from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = """
<Response>
    <Say language="pt-BR">
      E ai, beleza? Bora estudar python!
    </Say>
</Response>
"""

call = client.calls.create(
       twiml=message,
       to=os.environ.get("PHONE_TO"),
       from_=os.environ.get("PHONE_FROM"),
)

print(call.sid)
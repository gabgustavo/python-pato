from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

sid = os.getenv('TWILIO_SID')
token = os.getenv('TWILIO_TOKEN')
phone = os.getenv('TWILIO_PHONE')

client = Client(sid, token)

message = client.messages.create(
    body="Hola, este es mi mensaje de texto",
    from_=phone,
    to='+15078533151',
)

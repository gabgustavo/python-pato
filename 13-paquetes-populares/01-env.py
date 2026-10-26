from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
import os
from dotenv import load_dotenv

load_dotenv()

apiKey = os.getenv('SENDGRID_API_KEY')
email = os.getenv('SENDGRID_EMAIL')

message = Mail(
    from_email=email,
    to_emails='test-developer@mailinator.com',
    subject='Esta es una prueba de envio de correos',
    html_content='<strong>Probando</strong>')


try:
    send = SendGridAPIClient(apiKey)
    response = send.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(apiKey)
    print(e)

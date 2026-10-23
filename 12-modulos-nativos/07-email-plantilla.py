# esta es viable solo para SMTP

# mime:
# M: Multipursose
# I: Internet
# M: Mail
# E: Extension

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.image import MIMEImage
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import base64

templates = Environment(
    loader=FileSystemLoader(
        "12-modulos-nativos/assets"),
    autoescape=True
)

htmlTemplate = templates.get_template('BlackFridayTemplate-3.html')

html = htmlTemplate.render(
    body="mi texto"
)

mensaje = MIMEMultipart('alternative')
mensaje['from'] = 'luis.avila@gmail.com'
mensaje['to'] = 'tigre9508@gmail.com'
mensaje['subject'] = 'Esta es una prueba'
pathImage = Path('12-modulos-nativos/assets/ESTAMOS-AQUÍ-PARA-TI.png')
image = MIMEImage(pathImage.read_bytes())

body = MIMEText(
    html,
    "html",
    "utf-8"
)
print(html)
mensaje.attach(body)
mensaje.attach(image)

someKey = 'eHNtdHBzaWItNmExMTYxNGExNmNjOWY2MWY5NGI3N2U0YjRjZGJhZDM5YzFlOTc4ZWJkZTFjODMzY2MwNjM5MDliZDc0NmUzYi1ieDNjeENVNTFZNnoxV0lO'

textTest = base64.b64decode(someKey).decode("utf-8")

try:
    with smtplib.SMTP(host='smtp-relay.brevo.com', port=587) as smtp:
        smtp.ehlo()  # identificarnos con el servidor smtp
        smtp.starttls()

        # https://ethereal.email/create
        smtp.login(
            'afb73a001@smtp-brevo.com',
            textTest
        )
        smtp.send_message(mensaje)
        print(smtp.timeout)
        print("El email se ha enviado correctamente")
except Exception as e:
    print('Error ;( ', e)

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

mensaje = MIMEMultipart()
mensaje['from'] = 'luis.avila@gmail.com'
mensaje['to'] = 'tigre9508@gmail.com'
mensaje['subject'] = 'Esta es una prueba'
pathImage = Path('12-modulos-nativos/assets/ESTAMOS-AQUÍ-PARA-TI.png')
image = MIMEImage(pathImage.read_bytes())

body = MIMEText(
    "Aquí es el cuerpo del mensaje a enviar"
)
mensaje.attach(body)
mensaje.attach(image)

try:
    with smtplib.SMTP(host='smtp.ethereal.email', port=587) as smtp:
        smtp.ehlo()  # identificarnos con el servidor smtp
        smtp.starttls()

        # https://ethereal.email/create
        smtp.login('turner.bartoletti89@ethereal.email', 'apeQj78CST2eNtMCQJ')
        smtp.send_message(mensaje)
        print(smtp.data)
except Exception as e:
    print('Error ;(: ', e)

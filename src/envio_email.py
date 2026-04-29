from email.message import EmailMessage
from smtplib import SMTP

msg = EmailMessage()
msg['Subject'] = 'Assunto do email'
msg['From'] = 'sampacast_eventos@adesampa.com.br'
msg['To'] = 'carlos.morais@adesampa.com.br'
msg.set_content('Teste de mensagem')

with SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('sampacast_eventos@adesampa.com.br', ''.replace(' ', ''))
    smtp.send_message(msg)


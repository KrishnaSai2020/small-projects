import smtplib
from email.message import EmailMessage 
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'krishnasai'
email['to'] = 'krishnasai.chivukula@gmail.com'
email['subject'] = 'this is the subject of email'

email.set_content(html.substitute({'name':'tintin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('dummy54366@gmail.com', 'Fizzes27!')
	smtp.send_message(email)
	print('all good')


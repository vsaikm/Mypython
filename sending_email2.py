import smtplib #standard for  emails to be set to send the mails ,we need smtp server to snd emails 
from email.message import EmailMessage

#here we are introducing new modules

from string import  Template
from pathlib import Path 

html = Template(Path('index').read_text())
email = EmailMessage()
email['from'] = 'sai kumar'
email['to'] = 'sai281996@gmail.com'
email['subject'] = 'you won a 10000000 dollars'

email.set_content(html.substitute({'name' : 'sai'}),'html') #text #imagesetc
#smtp erver to login  to  email and send to to addrress

with smtplib.SMTP(host = 'smtp.gmail.com' , port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()#tls is an encrption mechanism,connect securely to the server
    smtp.login('saimvsk3@gmail.com', 'Sai@123#')
    smtp.send_message(email)
    print('all good boss')



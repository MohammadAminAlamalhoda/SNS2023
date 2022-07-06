import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

import codecs


def send_mail(info, file_name):
    
    name = info[0]
    user_name = info[2]
    user_pass = info[3]
    receiver_email = info[1]
    sender_email = "sharif.neuro.symposium2022@gmail.com"
    password = "4thyearSNS2022_jooje"
    smtp_server = "smtp.gmail.com"
    port = 465 
    context = ssl.create_default_context()


    message = MIMEMultipart("alternative")
    message["Subject"] = "SNS2022 Username and Password"
    message["From"] = sender_email
    message["To"] = receiver_email

    f = codecs.open(file_name, 'r')
    html = str(f.read())

    html = html.replace("!NAME!", name)
    html = html.replace("!USERNAME!", user_name)
    html = html.replace("!PASSWORD!", user_pass)
    # print(html)
    
    html = MIMEText(html, "html")
    message.attach(html)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

    # try:
    #     server = smtplib.SMTP(smtp_server,port)
    #     server.ehlo()
    #     server.starttls(context=context)
    #     server.ehlo()
    #     server.login(sender_email, password)
        
    # except Exception as e:
    #     print(e)
    # finally:
    #     server.quit() 
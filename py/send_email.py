import smtplib, ssl
import certifi
from email.message import EmailMessage


def send_message(username, email, message):
    port = 465
    content = username+" sent the following message: \n\n"+message+"\n\n--------\nEnd of message"
    context = ssl.create_default_context(cafile=certifi.where())
    server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
    server.login("nk.domainmanagement@gmail.com", "mymsy7-xofrAt-xajqon")
    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = 'PyPlutchik: New incoming message from '+username
    msg['From'] = email
    msg['To'] = "nk.domainmanagement@gmail.com"
    server.send_message(msg)
    server.quit
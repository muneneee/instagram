from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_welcome_email(username,receiver):
    subject = 'Welcome to Insta'
    sender = 'muneneeekev@gmail.com'

    text_content = render_to_string('email/welcomemail.txt', {"username":username})
    html_content = render_to_string('email/welcomemail.html', {"username":username})


    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
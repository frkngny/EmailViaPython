from myinfo import MYMAIL, MYPASSWORD
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


def send_mail(text='Text Body', subject='My Subject', from_email="My Name <YOURMAILADDRESS>", to_email=None, html=None):
    assert isinstance(to_email, list)
    message = MIMEMultipart('alternative')
    message["From"] = from_email
    message["To"] = ", ".join(to_email)
    message["Subject"] = subject

    body = MIMEText(text, 'plain')
    message.attach(body)

    if html is not None:
        my_html = MIMEText(html, 'html')
        message.attach(my_html)

    # image = open('yt.png', 'rb').read()
    # my_image = MIMEImage(image)
    # message.attach(my_image)

    message = message.as_string()

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(MYMAIL, MYPASSWORD)
    server.sendmail(from_email, to_email, message)
    server.quit()


if __name__ == '__main__':
    send_mail(text="Hello everyone! This is how you send an email.", subject='Message',
              to_email=['TOEMAIL'])



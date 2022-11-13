from rest_framework import status
from rest_framework.response import Response

from test_rocket.celery import app
from django.core.mail import EmailMessage, BadHeaderError, send_mail
from test_rocket.settings import EMAIL_HOST_USER


@app.task
def send_mail_task(path, email):
    msg = EmailMessage('QRCODE CREATE', 'QR', EMAIL_HOST_USER, [email])
    msg.attach_file(path=path)
    try:
        msg.send()
    except BadHeaderError:
        return Response({"Message": "Send Email error!"}, status=status.HTTP_400_BAD_REQUEST)

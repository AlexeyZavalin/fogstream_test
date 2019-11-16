import logging

from django.urls import reverse
from django.core.mail import send_mail
from fogstreamtest.celery import app

from django.conf import settings


@app.task
def send_message(message_id):
    # message = Message.objects.get(id=message_id)
    message = {
        'title': 'test title',
        'message': 'test text',
        'email': 'az@pf27.ru'
    }
    send_mail(message['title'], message['message'], settings.EMAIL_HOST_USER,
              [message['email']], fail_silently=False)

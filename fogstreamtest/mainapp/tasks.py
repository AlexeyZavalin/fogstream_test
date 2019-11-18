from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from mainapp.models import Message


@shared_task
def send_message(message_id):
    message = Message.objects.get(id=message_id)
    send_mail('Сообщение', message.message, 
    settings.EMAIL_HOST_USER, [message.email], fail_silently=False)

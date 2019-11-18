from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import urllib.request
import json


def find_email(email):
    """
    Функция для поиска email в списке
    :param email: строка с email для поиска
    :return: Информацию о пользователе
    """
    users_json = urllib.request.urlopen('http://jsonplaceholder.typicode.com/users')
    users = json.load(users_json)
    for user in users:
        if user['email'] == email:
            yield json.dumps(user)


@shared_task
def send_message(message):
    email_data = find_email(message.email)
    message_str = message.message
    if email_data:
        for item in email_data:
            message_str = f'{message_str} {item}'
    send_mail('Сообщение', message_str, 
    settings.EMAIL_HOST_USER, [message.email], fail_silently=False)
    message.status = 'SC'
    message.save()

from django.db import models
from django.db.models import signals
import urllib.request
import json

from mainapp.tasks import send_message


def find_email(email):
    """
    Функция для поиска email в списке
    :param email:
    :return: Словарь с информацией о пользователе
    """
    users_json = urllib.request.urlopen('http://jsonplaceholder.typicode.com/users')
    users = json.load(users_json)
    for user in users:
        if user['email'] == email:
            yield user


class Message(models.Model):
    STATUSES = [
        ('SC', 'Successfully'),
        ('US', 'Unsuccessfully'),
    ]

    email = models.EmailField(max_length=254)
    message = models.TextField()
    status = models.CharField(max_length=2, choices=STATUSES, default='US')

    def __str__(self):
        return f'{self.email} - {self.status}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


def message_post_save(sender, instance, signal, *args, **kwargs):
    email = instance.email
    message = instance.message
    email_data = find_email(email)
    if email_data:
        for item in email_data:
            message = message + ' ' + json.dumps(item)
        instance.message = message
        instance.save()
    send_message(instance.pk)


signals.post_save.connect(message_post_save, sender=Message)

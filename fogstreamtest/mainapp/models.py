from django.db import models
import urllib.request

from mainapp.tasks import send_message


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

    def save(self, *args, **kwargs):
        create_task = False
        if self.pk is None:
            create_task = True
        super().save(*args, **kwargs)
        if create_task:
            send_message(self)


    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

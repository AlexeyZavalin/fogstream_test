from django.db import models


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

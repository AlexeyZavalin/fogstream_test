from django.test import TestCase
from django.contrib.auth.models import User
from mainapp.models import Message


class MessageModelTest(TestCase):
    
    def setUp(self):
        User.objects.create_user(username='user', password='12345', 
                                 email='test@test.ru')
        Message.objects.create(email='test@test.ru', message='test')

    def test_email_label(self):
        message = Message.objects.get(id=1)
        field_label = message._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_message_label(self):
        message = Message.objects.get(id=1)
        field_label = message._meta.get_field('message').verbose_name
        self.assertEquals(field_label, 'message')

    def test_email_max_length(self):
        message = Message.objects.get(id=1)
        max_length = message._meta.get_field('email').max_length
        self.assertEquals(max_length, 254)

from django.test import TestCase
from mainapp.forms import MessageForm, UserRegisterForm
from django.contrib.auth.models import User
from django.test.client import Client


class MessageFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(email='test@test.ru', password='12345',
                                        username='user')
        user.save()

    def test_email_field(self):
        self.client.login(username='user', password='12345')
        email = 'test@test.ru'
        form_data = {'email': email, 'message': 'test'}
        form = MessageForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_message_field(self):
        message = 'test'
        form_data = {'email': 'test@test.ru', 'message': message}
        form = MessageForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_empty_email_field(self):
        self.client.login(username='user', password='12345')
        email = ''
        form_data = {'email': email, 'message': 'test'}
        form = MessageForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_empty_message_field(self):
        self.client.login(username='user', password='12345')
        message = ''
        form_data = {'email': 'test@test.ru', 'message': message}
        form = MessageForm(data=form_data)
        self.assertFalse(form.is_valid())


class RegisterFormTest(TestCase):
    
    def test_empty_email_field(self):
        form_data = {'username': 'user', 'password': '12345', 'email': ''}
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

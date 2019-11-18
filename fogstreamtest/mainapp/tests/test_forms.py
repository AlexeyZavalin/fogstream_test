from django.test import TestCase
from mainapp.forms import MessageForm
from django.contrib.auth.models import User


class MessageFormTest(TestCase):

    def SetUp(self):
        self.user = User.objects.create_user(email='test@test.ru', password='test5678',
                                   username='user')
        self.user.save()

    def test_email_field(self):
        email = 'test@test.ru'
        form_data = {'email': email, 'message': 'test'}
        form = MessageForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_message_field(self):
        message = 'test'
        form_data = {'email': 'test@test.ru', 'message': message}
        form = MessageForm(data=form_data)
        self.assertTrue(form.is_valid())

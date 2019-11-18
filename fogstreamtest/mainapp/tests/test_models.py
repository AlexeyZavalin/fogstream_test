from django.test import TestCase

from mainapp.models import Message


class MessageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Message.objects.create(email='test@test.ru', message='test')

    # def test_email_label(self):
    #     message = Message.objects.get(id=1)
    #     field_label = message._meta.get_field('email').verbose_name
    #     self.assertEquals(field_label, 'email')

    def test_email_max_length(self):
        message = Message.objects.get(id=1)
        max_length = message._meta.get_field('email').max_length
        self.assertEquals(max_length, 254)

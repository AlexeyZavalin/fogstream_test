from django.test import TestCase
from mainapp.models import Message

class MessageModelTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        # Очистка после каждого метода
        pass

    def test_email_label(self):
        message = Message.objects.get(id=1)
        

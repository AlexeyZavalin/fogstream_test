from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class MainViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='user', password='12345', 
                                        email='test@test.ru')
        user.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('mainapp:send_message'))
        self.assertRedirects(response, '/login?next=/message')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='user', password='12345')
        response = self.client.get(reverse('mainapp:send_message'))
        
        # Проверка что пользователь залогинился
        self.assertEqual(str(response.context['user']), 'user')
        # Проверка ответа на запрос
        self.assertEqual(response.status_code, 200)

        # Проверка того, что мы используем правильный шаблон
        self.assertTemplateUsed(response, 'mainapp/message.html')

    def test_send_message_view_without_login(self):
        # self.client.login(username='user', password='12345')
        response = self.client.get(reverse('mainapp:send_message'))
        self.assertEquals(response.status_code, 302)

    def test_send_message_view_with_login(self):
        self.client.login(username='user', password='12345')
        response = self.client.get(reverse('mainapp:send_message'))
        self.assertEquals(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get(reverse('mainapp:login'))
        self.assertEquals(response.status_code, 200)

    def test_register_view(self):
        response = self.client.get(reverse('mainapp:register_user'))
        self.assertEquals(response.status_code, 200)
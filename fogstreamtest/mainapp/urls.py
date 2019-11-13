from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('register', mainapp.UserCreateView.as_view(), name='register_user'),
    path('login', mainapp.user_login, name='login'),
    path('message', mainapp.MessageCreateView.as_view(), name='send_message')
]

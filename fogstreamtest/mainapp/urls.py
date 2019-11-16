from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('register', mainapp.UserCreateView.as_view(), name='register_user'),
    path('login', mainapp.UserSignIn.as_view(), name='login'),
    path('logout', mainapp.user_logout, name='logout'),
    path('message', mainapp.MessageCreateView.as_view(), name='send_message')
]

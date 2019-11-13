from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from mainapp.models import Message
import django.forms as forms


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('email', 'message')

    def clean_email(self):
        data = self.cleaned_data['email']
        if data == '':
            raise forms.ValidationError('Введите email')
        user = User.objects.filter(email=data).first()
        if user is None:
            raise forms.ValidationError('Пользователя с таким email не существует')
        return data

    def clean_message(self):
        data = self.cleaned_data['message']
        if data == '':
            raise forms.ValidationError('Введите сообщение')
        return data

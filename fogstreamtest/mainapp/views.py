from django.shortcuts import render, HttpResponseRedirect

from django.contrib.auth.forms import AuthenticationForm
from mainapp.forms import UserRegisterForm
from mainapp.forms import MessageForm
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from mainapp.models import Message

from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test

from django.http import JsonResponse

from django.core.mail import send_mail

from django.views.generic.edit import CreateView

from django.utils.decorators import method_decorator

from django.conf import settings

import urllib.request
import json


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class UserCreateView(AjaxableResponseMixin, CreateView):
    model = User
    success_url = reverse_lazy('mainapp:login')
    form_class = UserRegisterForm


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('mainapp:send_message'))
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'mainapp/login.html', context)


def index(request):
    return HttpResponseRedirect(reverse('mainapp:login'))


@method_decorator(user_passes_test(lambda u: u.is_authenticated), name='dispatch')
class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mainapp:send_message')
    template_name = 'mainapp/message.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        users_json = urllib.request.urlopen('http://jsonplaceholder.typicode.com/users')
        users = json.load(users_json)
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        title = 'Сообщение'
        send_mail(title, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
        return response

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

from django.views.generic.edit import CreateView, FormView

from django.utils.decorators import method_decorator

from django.conf import settings


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


class UserSignIn(AjaxableResponseMixin, FormView):
    form_class = AuthenticationForm
    template_name = 'mainapp/login.html'
    success_url = reverse_lazy('mainapp:send_message')

    def form_valid(self, form):
        user = authenticate(**form.cleaned_data)
        if user:
            login(self.request, user)
        return HttpResponseRedirect(reverse_lazy('mainapp:send_message'))


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('mainapp:send_message'))
    else:
        return HttpResponseRedirect(reverse('mainapp:login'))


@method_decorator(user_passes_test(lambda u: u.is_authenticated), name='dispatch')
class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mainapp:send_message')
    template_name = 'mainapp/message.html'


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))

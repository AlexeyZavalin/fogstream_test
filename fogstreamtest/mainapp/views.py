from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from django.views.generic.edit import CreateView

from django.utils.decorators import method_decorator


class UserCreateView(CreateView):
    model = User
    success_url = reverse_lazy('mainapp:login')
    form_class = UserCreationForm


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'mainapp/login.html', context)

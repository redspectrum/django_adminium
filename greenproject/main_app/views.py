from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from main_app.forms import UserForm


@login_required(login_url='main_app:login')
def news(request):
    return render(request, 'main_app/news.html')


def welcome(request):
    return render(request, 'main_app/welcome.html')


def index(request):
    name = 'Elon'
    return render(request, 'main_app/index.html', context={'name': name})

def login(request):
    user_form = UserForm()

    return render(request, 'main_app/login.html', context={
        'user_form': user_form
    })


def register(request):
    user_form = UserForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)

            user = authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password']
            )

            auth_login(request, user)
            return redirect('/welcome')


    return render(request, 'main_app/register.html', context={
        'user_form': user_form
    })

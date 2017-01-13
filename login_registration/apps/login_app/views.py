from django.shortcuts import render, redirect
from django.contrib import messages
from .models import LogUser

# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')

def create(request):
    result = LogUser.objects.register(request.POST)
    if result[0] == True:
        return redirect('/success')
    else:
        for error in result[1]:
            messages.error(request, error, extra_tags="register")
        return redirect('/')

def success(request):
    return render(request, 'login_app/success.html')

def login(request):
    result = LogUser.objects.login(request.POST)
    if result[0] == True:
        return redirect('/success')
    else:
        for error in result[1]:
            messages.error(request, error, extra_tags="login")
        return redirect('/')

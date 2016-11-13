from django.shortcuts import render, redirect
from models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')

def create(request):
    result = User.objects.register(request.POST)
    if result[0] == True:
        messages.success(request, result[1])
        user_login(request, result[1])
        return redirect(reverse('course:index'))
    else:
        for message in result[1]:
            messages.add_message(request, messages.INFO, message)
        return redirect(reverse('login:index'))

def login(request):
    result = User.objects.loginValid(request.POST)
    if result[0] == True:
        messages.success(request, result[1])
        user_login(request, result[1])
        return redirect(reverse('course:index'))
    else:
        messages.error(request, result[1])
        return redirect(reverse('login:index'))

def success(request):
    if 'user' not in request.session:
        return redirect(reverse('login:index'))
    else:
        return redirect(reverse('course:index'))

def user_login(request, user):
    request.session['user'] = {
        'id':user.id,
        'first':user.first_name,
        'last':user.last_name,
        'email':user.email
    }
    return redirect(reverse('course:index'))

def logout(request):
    request.session.clear()
    return redirect(reverse('login:index'))

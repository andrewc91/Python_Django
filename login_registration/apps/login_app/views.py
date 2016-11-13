from django.shortcuts import render, redirect
from models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')

def create(request):
    result = User.objects.register(request.POST)
    if result[0] == True:
        messages.success(request, result[1])
        user_login(request, result[1])
        return redirect('/success')
    else:
        for message in result[1]:
            messages.add_message(request, messages.INFO, message)
        return redirect('/')

def login(request):
    result = User.objects.loginValid(request.POST)
    if result[0] == True:
        messages.success(request, result[1])
        user_login(request, result[1])
        return redirect('/success')
    else:
        messages.error(request, result[1])
        return redirect('/')

def success(request):
    if 'user' not in request.session:
        return redirect('/')
    else:
        return render(request, 'login_app/success.html')

def user_login(request, user):
    request.session['user'] = {
        'id':user.id,
        'first':user.first_name,
        'last':user.last_name,
        'email':user.email
    }
    return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect('/')

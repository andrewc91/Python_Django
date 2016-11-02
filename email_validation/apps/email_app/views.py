from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'email_app/index.html')

def process(request):
    if request.method == 'POST':
        result = User.objects.validEmail(request.POST['email'])

        if result[0]:
            messages.success(request, 'The email address you entered ({}) is a VALID email address! Thank you!'.format(result[1].email))
            return redirect('/success')
        else:
            for error in result[1]:
                messages.error(request, error)
            return redirect('/')

def success(request):
    context = {
        'data': User.objects.all()
    }
    return render(request, 'email_app/success.html', context)

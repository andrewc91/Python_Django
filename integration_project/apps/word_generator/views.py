from django.shortcuts import render, redirect
import random
import string

def random_words(size=14, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for word in range(size))

# Create your views here.
def index(request):
    if 'attempts' not in request.session:
        request.session['attempts'] = 1

    return render(request,'word_generator/index.html')

def create(request):
    if request.method == "POST":
        request.session['word'] = random_words(14)
        request.session['attempts'] += 1
        return redirect('/')
    else:
        return redirect('/')

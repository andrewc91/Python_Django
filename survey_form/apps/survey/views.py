from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
    return render(request, 'survey/index.html')

def create(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        request.session['attempts'] += 1
        return redirect('/result')
    else:
        return redirect('/')

def result(request):
    return render(request, 'survey/result.html')

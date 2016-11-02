from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
        "courses" : Course.objects.all()
    }
    return render(request, 'course_app/index.html', context)

def process(request):
        Course.objects.create(course_name=request.POST['name'], description=request.POST['description'])
        return redirect('/')

def delete(request,id):
    context = {
        'data' : Course.objects.get(id=id)
    }
    return render(request, 'course_app/delete.html', context)

def destroy(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')

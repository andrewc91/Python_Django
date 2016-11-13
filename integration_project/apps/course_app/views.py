from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Course
from ..login_app.models import User

# Create your views here.
def index(request):
    context = {
        "courses" : Course.objects.all()
    }
    return render(request, 'course_app/index.html', context)

def process(request):
        Course.objects.create(course_name=request.POST['name'], description=request.POST['description'])
        return redirect(reverse('course:index'))

def delete(request,id):
    context = {
        'data' : Course.objects.get(id=id)
    }
    return render(request, 'course_app/delete.html', context)

def destroy(request, id):
    Course.objects.get(id=id).delete()
    return redirect(reverse('course:index'))

def users_courses(request):
    context = {
        'courses': Course.objects.all(),
        'users': User.objects.all()
    }
    return render(request,'course_app/users_courses.html', context)

def assign(request):
    this_user = User.objects.get(id=request.POST['user_id'])
    this_course = Course.objects.get(id=request.POST['course_id'])
    this_course.users.add(this_user)
    return redirect(reverse('course:users_courses'))

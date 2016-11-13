from django.shortcuts import render, redirect
from .models import Course, User
from django.core.urlresolvers import reverse

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

# def usercourse(request):
#     if request.method=='POST':
#         Course.objects.AddUser(request.POST)
#         if Course.objects.AddUser(request.POST) == False:
#             messages.error(request, 'User already in this course')
#     context = {
#     'courses' : Course.objects.all(),
#     'users' : User.objects.all()
#     }
#     return render(request, 'course_app/user_course.html', context)

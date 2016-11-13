from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mh_user/user_course.html')

def usercourse(request):
    if request.method=='POST':
        Course.objects.AddUser(request.POST)
        if Course.objects.AddUser(request.POST) == False:
            messages.error(request, 'User already in this course')
    context = {
    'courses' : Course.objects.all(),
    'users' : User.objects.all()
    }
    return render(request, 'coursecreator/users_courses.html', context)

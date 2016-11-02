from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'ninja_turtle/index.html')

def show(request):
    return render(request, 'ninja_turtle/show.html')

def disappear_ninja(request, ninja_color):
    context = {
        'ninja_color': ninja_color,
        'blue': 'leonardo.jpg',
        'purple': 'donatello.jpg',
        'red': 'raphael.jpg',
        'orange': 'michelangelo.jpg',
    }
    return render(request, 'ninja_turtle/ninjas.html', context)

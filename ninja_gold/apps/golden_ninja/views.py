from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0

    if 'activities' not in request.session:
        request.session['activities'] = ""

    return render(request, 'golden_ninja/index.html')

def process(request):
    if request.method == 'POST':
        building = request.POST['building']
    # print building

    if (building == 'farm'):
        gold = random.randrange(10, 21)

    elif (building == 'cave'):
        gold = random.randrange(2, 11)

    elif (building == 'house'):
        gold = random.randrange(2, 6)

    elif (building == 'casino'):
        gold = random.randrange(-50, 51)

    if (gold > 0):
        activity = "Earn " + str(gold) + " golds from the " + building + "!"
    else:
        activity = "Went to the casino and lost " + str(gold) + " golds...yikes!"

    request.session['gold'] += gold
    request.session['activities'] += activity

    return redirect('/')

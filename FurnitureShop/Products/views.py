from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from . models import Studyroom, Livingroom

# Create your views here.
def Home(request):
    return HttpResponse(" I am form Poducts home")


# ---------Living Room-------------------------------------
def living(request):
    livingrooms = Livingroom.objects.all()

    context = {
        'livingrooms': livingrooms
    }
    return render(request,'livingroom.html', context)


# ---------Study Room-------------------------------------
def studyroom(request):
    studyrooms=Studyroom.objects.all()

    context = {
        'studyrooms': studyrooms
    }
    return render(request,'studyroom.html', context) 

# ---------Order -------------------------------------
def order(request,pk):
    livingitem1=Livingroom.objects.filter(id = pk)
    context = {
        'livingitem1': livingitem1
    }
    return render(request,'order.html', context) 



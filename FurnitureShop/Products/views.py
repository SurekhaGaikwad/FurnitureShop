from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from . models import Studyroom

# Create your views here.
def Home(request):
    return HttpResponse(" I am form Poducts home")

def living(request):
    return render(request,'living.html')

def studyroom(request):
    studyrooms=Studyroom.objects.all()
    return render(request,'studyroom.html',{'studyrooms':studyrooms}) 
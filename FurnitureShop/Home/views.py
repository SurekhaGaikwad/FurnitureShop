from django.shortcuts import render
from Products.models import Studyroom, Livingroom

# Function for filer to discpunt item
def Home(request):
    livingroom = Livingroom.objects.filter(Discount__gte = 1)
    studyroom = Studyroom.objects.filter(Discount__gte = 1)

    context = {        
            'livingroom':livingroom,
            'studyroom':studyroom
            }

    return render(request,'home.html', context)


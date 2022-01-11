from django.shortcuts import render
from Products.models import Studyroom, Livingroom
def Home(request):
    livingroom = Livingroom.objects.filter(Discount__gte = 1)
    studyroom = Studyroom.objects.filter(Discount__gte = 1)

    context = {        
            'livingroom':livingroom,
            'studyroom':studyroom
            }

    return render(request,'home.html', context)

# def DiscountItem(request):
    # livingroom = Livingroom.objects.get(Discount__gte = 0 )
    # studyroom = Studyroom.objects.filter(Discount__gte = 0)
  

# Create your views here.


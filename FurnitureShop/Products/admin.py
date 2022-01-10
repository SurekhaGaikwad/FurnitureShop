from django.contrib import admin
from .models import Studyroom, Livingroom
# Register your models here.

class studyadmin(admin.ModelAdmin):
    List_display=('ProductID',' Title','AMT','Discount','IMG')


# ---------Study Room-------------------------------------
admin.site.register(Studyroom,studyadmin)

# ---------Living Room-------------------------------------
admin.site.register(Livingroom,studyadmin)

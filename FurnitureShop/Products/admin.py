from django.contrib import admin
from .models import Studyroom
# Register your models here.

class studyadmin(admin.ModelAdmin):
    List_display=('ProductID',' Title','AMT','Discount','IMG')

admin.site.register(Studyroom,studyadmin)

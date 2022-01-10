from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name="ProductHome"),
    path('Living/',views.living,name="living"),
    path('Studyroom/',views.studyroom,name="studyroom"),
]
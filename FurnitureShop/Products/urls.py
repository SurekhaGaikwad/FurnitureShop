from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name="ProductHome"),
    path('living/',views.living,name="living"),
]
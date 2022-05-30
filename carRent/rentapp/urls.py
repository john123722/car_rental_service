from django.contrib import admin
from django.urls import path
from rentapp import views

urlpatterns = [
    path("",views.index,name='index'),
    path("contactus",views.contactus,name='contactus'),
    path("home",views.home,name='home'),
    path("view",views.view,name='view')
]

from django.contrib import admin
from django.urls import path
from rentapp import views

urlpatterns = [
    path("",views.login,name='login'),
    path("carrental",views.carrental,name='carrental'),
    path("contactus",views.contactus,name='contactus'),
    path("home",views.home,name='home'),
    path("view",views.view,name='view'),
    path("login",views.index,name='index'),
    path("logout",views.logout,name='logout')
]

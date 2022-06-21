from django.contrib import admin
from django.urls import path
from django.views import View
from rentapp import views

urlpatterns = [
    path("",views.login,name='login'),
    path("carrental",views.carrental,name='carrental'),
    path("contactus",views.contactus,name='contactus'),
    path("home",views.home,name='home'),
    path("view/<int:pk>",views.car_view.as_view(),name='car_view'),
    path("login",views.index,name='index'),
    path("logout",views.logout,name='logout')
]

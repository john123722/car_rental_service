from multiprocessing import context
from unicodedata import name
from django import views
from django.shortcuts import render
from datetime import datetime

from requests import request
from rentapp.models import Contact,car,reviews
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views import View

# Create your views here.
def logout(request):
    return render(request,'login.html')
def carrental(request):
    return render(request,'index.html')
def index(request):
    return render(request ,'index.html') 
def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        reason = request.POST.get('reason')
        
        contact = Contact(name=name, email=email, contact=contact,reason = reason, date = datetime.today())
        contact.save()
        messages.success(request, 'Message sent successfully')
    return render(request , 'contactus.html')

def home(request):
    context = {'cars':car.objects.all}
    return render(request,'home.html',context)


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username= username, password=password)
        if user is not None:
            messages.success(request, 'login successful')
            return render(request,'index.html')
        else:
            messages.warning(request, 'invalid username or password')
            return render(request,'login.html')
    return render(request,'login.html')



class car_view(View):
    def get(self,request, pk):
        context = {'cars':car.objects.filter(pk=pk)}
        return render(request,'view.html',context)
    




class rating_view(View):
    def get(self,request,pk):
        context = {'cars':car.objects.filter(pk=pk)
                   }
       
        return render(request,'rating.html',context)

    def post(self,request,pk):
        if request.method == "POST":
            username = request.POST.get('username')
            car_name = request.POST.get('car_name')
            rating = request.POST.get('rating')
            review = request.POST.get('review')
            review1 = reviews( username=username,car_name=car_name,rating=rating, review = review)
            review1.save()  
        
        context = {'revi':reviews.objects.all}
        return render(request,'rating.html',context)
     
     
         
    
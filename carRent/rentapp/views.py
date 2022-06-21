from django import views
from django.shortcuts import render
from datetime import datetime
from rentapp.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


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
    return render(request, 'home.html')




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



class car_view(views.View):
    def get(self,request, pk):
        View12 = View12.objects.get(pk = pk)
        return render(request,'view.html',{'View12':View12})
        
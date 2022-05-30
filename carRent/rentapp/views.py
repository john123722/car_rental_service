from django.shortcuts import render
from datetime import datetime
from rentapp.models import Contact
from django.contrib import messages
# Create your views here.
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
def view(request):
    return render(request, 'view.html') 
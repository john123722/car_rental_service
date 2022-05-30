from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request ,'index.html') 
def contactus(request):
    return render(request , 'contactus.html')
def home(request):
    return render(request, 'home.html')
def view(request):
    return render(request, 'view.html') 
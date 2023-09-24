from django.shortcuts import render, HttpResponse
from datetime import datetime
from MyApp.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    # messages.success(request, "This is a test")
    return render(request, 'index.html')
    

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        textarea = request.POST.get('textarea')
        contact = Contact(name=name, email=email, password=password, textarea=textarea, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent !")
    return render(request, 'contact.html') 
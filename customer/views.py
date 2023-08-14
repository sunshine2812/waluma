from customer.models import Customer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User
from .models import Customer



# Create your views here

def index (request):
    return render(request, "customer/index.html")

def connection(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login (request,user)
            return redirect('home')
        else:
            return render(request, 'customer/connection.html', {'error': 'identifiant invalide. Veuillez réessayer'})

    return render(request, "customer/connection.html")

def inscription(request):
    if request.method == 'POST':
        account_number = request.POST['account_number']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        username = request.POST['username']
        password = request.POST['password']

        if Customer.objects.filter(account_number=account_number).exists():
            return render(request, 'customer/inscription.html', {'error': 'Ce numéro de compte existe déjà.'})

        user = User.objects.create_user(username=username, email=email, password=password)

        customer = Customer.objects.create(account_number=account_number, email=email, phone_number=phone_number, username=username, password=password)

        return redirect('connection')  

    return render(request, 'customer/inscription.html')
    

def home(request):
    return render(request, "customer/home.html")



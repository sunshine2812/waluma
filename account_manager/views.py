from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from account_manager.models import Account_manager
from complain.models import Complain,Nature

def create_account(request):
    if request.method == 'POST':
        lastname = request.POST['lastname']
        firstname = request.POST['firstname']
        username = request.POST['username']
        password = request.POST['password']
        phone_number = request.POST.get('phone_number', '')
        role_id = request.POST['role']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d\'utilisateur existe déjà.')
            return redirect('inscription-manager')

        user = User.objects.create_user(username=username, password=password)
        
        try:
            role = Nature.objects.get(pk=role_id)
            account_manager = Account_manager(
                lastname=lastname,
                firstname=firstname,
                username=username,
                password=password,
                phone_number=phone_number,
                role=role
            )
            account_manager.save()
            messages.success(request, 'Le compte a été créé avec succès.')
            return redirect('connection-manager')
        except Nature.DoesNotExist:
            messages.error(request, 'Le rôle sélectionné n\'existe pas.')
            return redirect('connection-manager')

    roles = Nature.objects.all()
    return render(request, 'account_manager/create_account.html', {'roles': roles})

        

         

def connection_manager(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login (request,user)
            return redirect('show')
        else:
           messages.error(request,  'identifiant invalide. Veuillez réessayer')

    return render(request, "account_manager/connection.html")

def show(request):
    if request.user.is_authenticated:
        account_manager = Account_manager.objects.get(username=request.user.username)
        role_id = account_manager.role.id_nature

        # Récupérer toutes les réclamations où l'id_nature correspond au rôle de l'account_manager
        complaints = Complain.objects.filter(id_nature=role_id)
        nature = Nature.objects.get(pk=role_id)

        return render(request, 'account_manager/show.html', {'complaints': complaints, 'nature': nature})
    else:
        return redirect('connection-manager')
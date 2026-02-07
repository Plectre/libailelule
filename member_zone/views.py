from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LogForm
from .models import Logs

def login_view(request):
    print("login_view")
    return render(request, 'member_zone/login.html')

def login_request(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authentifier l'utilisateur
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('hangar') 
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'member_zone/login.html')

def logout_request(request):
    print("logout is comming")
    logout(request)
    return redirect('index')

@login_required
def hangar(request):
    # check if authenticated
    if request.user.is_authenticated:
        log = Logs.objects.filter(pilot=request.user)
        return render(request, 'member_zone/hangar.html', {'logs': log})
    else:
        return redirect('index')
    
@login_required   
def form_log(request):
    if request.method == 'POST':
        form_log = LogForm(request.POST)
        if form_log.is_valid():
            form_log = form_log.save(commit=False) 
            form_log.pilot = request.user
            print(form_log.pilot)
            form_log.save()
            return redirect ('hangar')
        else:
            print(form_log.errors)
            return redirect('form_log')
    else:
        form = LogForm()
        return render(request,'member_zone/form_log.html', {'form' : form})

def edit_log(request):
    if request.method == "POST":
        pk = request.POST.get('pk')

def delete_log(request):
    print("suprimer Log")
    pass
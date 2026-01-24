from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    print("login_view")
    return render(request, 'login.html')

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
    return render(request, 'login.html', {'user' :user.username})

def logout_request(request):
    print("logout is comming")
    logout(request)
    return redirect('index')

def hangar(request):
    # check if authenticated
    if request.user.is_authenticated:
        return render(request, 'hangar.html')
    else:
        return redirect('index')
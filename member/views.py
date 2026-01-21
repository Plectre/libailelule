from django.shortcuts import render
from django.contrib.auth.models import User

def form(request):

    users = User.objects.all()
    print(users)
    return render(request, 'form.html', {'users' : users})



from django.shortcuts import render
from .models import Articles as article
from .models import Carte

def index(request):  
    cartes = Carte.objects.all()
    return render(request, 'page/carte.html', {"cartes" : cartes})


def club(request):
    return render(request, "page/club.html", context={"club":"club",})

def base(request):
    return render(request, "page/base.html")
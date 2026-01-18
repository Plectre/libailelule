
from django.shortcuts import render
from .models import Articles as article

def index(request):
    
    context = {}
    instance = article.objects.all()
    return render(request, 'page/index.html', {"context" : instance})


def club(request):
    return render(request, "page/club.html", context={"club":"club",})

def base(request):
    return render(request, "page/base.html")
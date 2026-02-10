from django.shortcuts import render

def planning_loc(request):
    return render(request, "planning_loc/calandar.html")

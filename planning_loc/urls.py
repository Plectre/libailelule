from . import views
from django.urls import path

urlpatterns=[
    path('planning_loc/calandar/', views.planning_loc, name="calandar"),
]
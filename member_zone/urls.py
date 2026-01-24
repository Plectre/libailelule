from django.urls import path

from . import views

urlpatterns = [
    path('member/login/', views.login_view, name="member_login"),
    path('member/request/', views.login_request, name="login_request"),
    path('member/logout/', views.logout_request, name="logout_request"),
    path('member/hangar/', views.hangar, name="hangar"),
]
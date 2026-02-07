from django.urls import path

from . import views


urlpatterns = [
    path('member/login/', views.login_view, name="member_login"),
    path('member/request/', views.login_request, name="login_request"),
    path('member/logout/', views.logout_request, name="logout_request"),
    path('member/hangar/', views.hangar, name="hangar"),
    path('member/form_log/', views.form_log, name='form_log'),
    path('member/edit_log/', views.edit_log, name='edit_log'),
    path('member/delete_log/', views.delete_log, name='delete_log'),
]
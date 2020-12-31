from django.urls import path, include
from . import views

app_name = "login"
urlpatterns = [
    path('', views.login_redirect, name="redirectToLogin"),
    path('login', views.login, name="login"),
    path('process_regi', views.process_regi),
    path('process_login', views.process_login),
    path('logout', views.logout, name="logout"),
    # path('process_user_info_change/', views.process_user_info_change),
    # path('process_user_pw_change/', views.process_user_pw_change),
    path('delete_user/<user_id>/', views.confirm_delete, name="delete"),
    path('delete_user/<user_id>/confirm/', views.delete_user, name="confirmDelete"),
]

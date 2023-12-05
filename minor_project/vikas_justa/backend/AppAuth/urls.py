from django.urls import path
from . import views

urlpatterns = [
    path("", views.auth_home, name=""),
    path("login/", views.auth_login, name=""),
    path("login/login_handler", views.login_handler, name=""), 
    path("signup/signup_handler", views.signup_handler, name=""), 
    path("signup/", views.auth_signup, name=""),    

]

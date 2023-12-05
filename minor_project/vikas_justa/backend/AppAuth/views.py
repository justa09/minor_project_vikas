from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def auth_home(req: HttpRequest)-> HttpResponse:
    return HttpResponse("hello world")


def auth_login(req: HttpRequest):
    return render(req, "login_.html")

def auth_signup(req: HttpRequest):
    return render(req, "signup.html")

def signup_handler(req:HttpRequest):
    uname = req.POST.get('uname')
    first_name = req.POST.get('fname')
    last_name = req.POST.get('lname')
    email = req.POST.get('email')
    password = req.POST.get('password')
    c_password = req.POST.get('cpassword')
    print(uname, first_name, last_name, email, password, c_password)
    if password!=c_password:
        print("passwords doesnt match")
        return HttpResponse("password doesnt match")
    
    try:
        user = User.objects.get(username=uname)
        print(user)

    except:
        print("user doesnt exist")
        user = User.objects.create_user(
            username=uname, 
            email=email, 
            password=password, 
            first_name=first_name, 
            last_name=last_name
        )

        if user:
            return HttpResponse("user created sucessfully")


def login_handler(req: HttpRequest):
    username = req.POST.get("uname")
    password = req.POST.get('password')
    user = authenticate(req, username=username, password=password)
    print(user)
    if user is not None:
        login(req, user)
        print("loged in")
    
    print(f"{username=}, {password=}")
    return redirect("/")

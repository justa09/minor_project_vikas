from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from Project.models import Company
from django.contrib.auth.models import User

def home(req:HttpRequest):
    if req.method == "GET":
        print(req.user)
        print("hello")
    elif req.method == "POST":
        ...
    return render(req, "index.html", {"user": req.user})

def company_profile(req: HttpRequest):
    return render(req, "company_profile.html")

def company2_profile(req: HttpRequest):
    return render(req, "company2.html")


def sitemap(req):
    return render(req, "sitemap.html")

def get_hired(req: HttpRequest):
    return render(req, "hire_form.html")

def register_company(req: HttpRequest):
    return render(req, "register_company.html")

def register_handler(req: HttpRequest):
    if req.method =="POST":
        print(req.body)
        company_name = req.POST.get("name")
        company_email = req.POST.get("email")
        company_desc = req.POST.get("desc")
        company_founded = req.POST.get("founded")
        company_ceo = req.POST.get("ceo")
        company_hq = req.POST.get("hq")
        print(company_ceo, company_desc, company_email)


        company = Company.objects.create(
            name=company_name,
            email=company_email,
            desc=company_desc,
            founded_date=company_founded,
            ceo=company_ceo,
            hq=company_hq
            )

        company.save()

        return HttpResponse("Company registered sucessfully")

def recruiter_dashboard(req: HttpRequest):
    users = list(User.objects.filter(is_superuser=False))
    # users = list(User.objects.all())
    print(users)
    return render(req, "recruiter_dashboard.html", {"user_list": users})

def job(req: HttpRequest)-> HttpResponse:
    return render(req, "job.html")


def employee(req: HttpRequest)-> HttpResponse:
    return render(req, "employee.html")


def clients(req: HttpRequest)-> HttpResponse:
    return render(req, "clients.html")


def help(req: HttpRequest)-> HttpResponse:
    return render(req, "help.html")

def career(req: HttpRequest)-> HttpResponse:
    return render(req, "career.html")

def home2(req: HttpRequest)-> HttpResponse:
    return render(req, "home.html")


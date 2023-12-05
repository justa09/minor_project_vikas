from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# from .models import Project

# Create your views here.
def home(req: HttpRequest)-> HttpResponse:
    return HttpResponse("hello")


def post_project(req: HttpRequest)-> HttpResponse:
    return render(req, "post_project.html")
    return HttpResponse("this is post project")

def post_project_handler(req: HttpRequest)-> HttpResponse:
    # if req.method == "POST":
    #     project_title = req.POST.get("project_title")
    #     project_description = req.POST.get("project_description")
    #     print(project_title, project_description)
    #     pr = Project.objects.create(project_title=project_title, project_description=project_description)
    #     pr.save()
    #     return HttpResponse("submitted")
    ...

from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.home),
    path("post-project/", views.post_project),
    path("post_project_handler/", views.post_project_handler),
]

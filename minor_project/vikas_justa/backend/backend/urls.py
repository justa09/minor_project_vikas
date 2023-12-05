from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.home),
    path("auth/", include("AppAuth.urls"), name=""),
    path('admin/', admin.site.urls),
    path('projects/', include("Project.urls")),
    path("sitemap/", views.sitemap),
    path("company_profile/", views.company_profile),
    path("company2/", views.company2_profile),
    path("get-hired/", views.get_hired),
    path("register-company/", views.register_company),
    path("register-company/register/", views.register_handler),
    path("recruiter-dashboard", views.recruiter_dashboard),
    path("job/", views.job),
    path("employee/", views.employee),
    path("clients/", views.clients),
    path("help/", views.help),
    path("career/", views.career),
    path("home2/", views.home2),
]

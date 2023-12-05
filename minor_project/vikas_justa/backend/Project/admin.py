from django.contrib import admin
from .models import Company
# from .models import Resume, Project, Department, Employee, Organisation, Recruiter
# Register your models here.
from .models import Employee

# admin.site.register(Project)
# admin.site.register(Department)
admin.site.register(Employee)
# admin.site.register( Organisation)
# admin.site.register(Recruiter)
# admin.site.register(Resume)
admin.site.register(Company)
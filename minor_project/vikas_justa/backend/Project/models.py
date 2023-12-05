from django.db import models
from AppAuth.models import Profile
import utils
from django.urls import reverse
from django.contrib.auth.models import User


# project table
# class Project(models.Model):
#     project_title = models.CharField(max_length=100)
#     project_description = models.TextField()
#     date = models.DateField(auto_now_add=True)
#     project_id = models.IntegerField(null=True, blank=True)

#     class Meta:
#         verbose_name = ("project")
#         verbose_name_plural = ("projects")
  
#     def __str__(self):
#         return self.project_title

#     def get_absolute_url(self):
#         return reverse("project_detail", kwargs={"pk": self.pk})


#resume table
class Resume(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = models.TextField()
    projects_done = models.TextField()

    class Meta:
        verbose_name = ("resume")
        verbose_name_plural = ("resumes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("resume_detail", kwargs={"pk": self.pk})


#organisation table
class Organisation(models.Model):
    org_id = models.IntegerField()
    org_name = models.CharField(max_length=50)
    org_address = models.TextField()

    def __str__(self) -> str:
        return self.org_name
    

# Department Table
class Department(models.Model):
    dept_id = models.IntegerField()
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Department")
        verbose_name_plural = ("Departments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Department_detail", kwargs={"pk": self.pk})


# Employee table
class Employee(models.Model):

    emp_id = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    dept_id = models.IntegerField()
    dob = models.DateField()
    address = models.TextField()
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})


# client table 
class Client(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    phno = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("client")
        verbose_name_plural = ("clients")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("client_detail", kwargs={"pk": self.pk})


# recruiter table
class Recruiter(models.Model):

    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    org = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("recruiter")
        verbose_name_plural = ("recruiters")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recruiter_detail", kwargs={"pk": self.pk})

#Freelancer table
class Freelancer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("freelancer")
        verbose_name_plural = ("freelancers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("freelancer_detail", kwargs={"pk": self.pk})
    

class Company(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    desc = models.TextField()
    founded_date = models.IntegerField()
    ceo = models.CharField(max_length=50)
    hq = models.CharField(max_length=100)

    def __str__(self):
        return self.name

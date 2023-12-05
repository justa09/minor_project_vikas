from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class UserType(models.Model):
    CHOICES = (
        ('e', 'employee'),
        ('r', 'recruiter'),
        ('f', 'freelancer'),
        ('c', 'client'),
    )

    name = models.CharField(max_length=1, choices=CHOICES)

    class Meta:
        verbose_name = "User Type"
        verbose_name_plural = "User Types"
    
    def __str__(self) -> str:
        return self.name
    


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.FileField(upload_to="media/")
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Profile_detail", kwargs={"pk": self.pk})


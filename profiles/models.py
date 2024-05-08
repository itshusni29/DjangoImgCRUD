from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    Division = models.CharField(max_length=100, blank=True)
    Department = models.CharField(max_length=100, blank=True)
    Section = models.CharField(max_length=100, blank=True)
    Occupation = models.CharField(max_length=100, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)

    def __str__(self):
        return self.user.username
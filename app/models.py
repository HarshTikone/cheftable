from djongo import models
from django.contrib.auth.models import User


class Profile(models.Model):
    username = models.CharField(max_length=100)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    profile_img = models.ImageField(max_length=100, default="profile_images.png")

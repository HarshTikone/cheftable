from djongo import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=1000, null=True)
    profile_img = models.ImageField(max_length=100, default="profile_images.png")


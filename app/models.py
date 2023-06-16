from djongo import models


class Profile(models.Model):
    username = models.CharField(max_length=100)
    id_user = models.IntegerField()
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    profile_img = models.ImageField(max_length=100, default="profile_images.png")

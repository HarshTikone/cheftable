from djongo import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=1000, null=True)
    profile_img = models.ImageField(max_length=100, default="profile_images.png")

def upload_to(instance, filename):
    username = instance.user.username
    recipename = instance.recipe_name.replace(" ", "_")
    return f'media/post_images/{username}_{recipename}.jpg'

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=100)
    ingredients = models.TextField()
    steps_to_make = models.TextField()
    average_cooking_time = models.PositiveIntegerField()
    servings = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_to)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipe_name


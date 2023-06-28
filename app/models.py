from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recipe(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    recipe_name=models.CharField(max_length=50)
    recipe_description=models.TextField(blank=True,null=True)
    recipe_image=models.ImageField(blank=True,null=True,upload_to="images")


    def __str__(self):
        return self.recipe_name
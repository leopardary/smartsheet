from django.db import models
from .. import Metrology

#this model contains all recipes, but only gives name and discription. Should include the method for parsing result.

class Recipe(models.Model):
    recipename=models.CharField(max_length=200)
    measureType=models.CharField(max_length=100)
    metrology=models.ForeignKey(Metrology, on_delete=models.SET_NULL,blank=True,null=True)
    description=models.CharField(max_length=1000,blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)

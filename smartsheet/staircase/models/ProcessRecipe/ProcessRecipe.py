from django.db import models

import pandas as pd
from .. import Chamber
from .Raw_recipe_file import Raw_recipe_file

from datetime import datetime

class ProcessRecipe(models.Model):
    recipeName=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    recipeNote=models.CharField(max_length=200)
    recipeDetail=models.CharField(max_length=1000)
    recipeFile=models.ForeignKey(Raw_recipe_file,on_delete=models.SET_NULL,null=True,blank=True)
    chamber=models.ForeignKey(Chamber,on_delete=models.SET_NULL,null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)    #creation time
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)  #update time
    def __str__(self):
        return self.recipeName

    class Meta:
        abstract=True
    


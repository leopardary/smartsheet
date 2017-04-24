from django.db import models

import pandas as pd

from datetime import datetime

class ProcessRecipe(models.Model):
    recipeName=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    recipeNote=models.CharField(max_length=200)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)    #creation time
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)  #update time

    def __str__(self):
        return self.recipeName
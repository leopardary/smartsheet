from django.db import models
from .. import Recipe
from .. import Split
from .. import Raw_data_file

class Thickness(models.Model):
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)
    recipe=models.ForeignKey(Recipe,on_delete=models.SET_NULL,blank=True,null=True)
    rawthk=models.CharField(max_length=10000,blank=True,null=True)
    rawX=models.CharField(max_length=10000,blank=True,null=True)
    rawY=models.CharField(max_length=10000,blank=True,null=True)
    rawRI=models.CharField(max_length=10000,blank=True,null=True)
    rawGOF=models.CharField(max_length=10000,blank=True,null=True)
    note=models.CharField(max_length=1000,blank=True,null=True)
    split=models.ForeignKey(Split,on_delete=models.SET_NULL,blank=True,null=True)
    rawDataFile=models.ForeignKey(Raw_data_file,on_delete=models.SET_NULL,blank=True,null=True)


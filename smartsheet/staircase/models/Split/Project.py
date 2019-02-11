from django.db import models

from .. import User

class Project(models.Model):
    projectName=models.CharField(max_length=100)
    projectDescription=models.CharField(max_length=1000)
    projectOwner=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    supportingProject=models.ManyToManyField('self')
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)

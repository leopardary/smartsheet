from django.db import models

from .. import User
from .. import Wafer,Foup_slot
from .. import Chamber
from .. import ProcessRecipe
from .. import Project


class Split(models.Model):
    wafer=models.ForeignKey(Wafer,on_delete=models.SET_NULL,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    foup_slot=models.ForeignKey(Foup_slot,on_delete=models.SET_NULL,null=True,blank=True)
    chamber=models.ForeignKey(Chamber,on_delete=models.SET_NULL,null=True,blank=True)
    processRecipe=models.ForeignKey(ProcessRecipe,on_delete=models.SET_NULL,null=True,blank=True)
    note=models.CharField(max_length=300,null=True,blank=True)
    followingProcess=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)   #if the current split is followed by another split on the same wafer, then this link is to that split
    project=models.ForeignKey(Project,on_delete=models.SET_NULL,null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)    #creation time
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)  #update time
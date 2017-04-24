from django.db import models

#this class stores all metrology info, eg. Aleris for thk/bow, WS2 for IPD, FTIR tool
class Metrology(models.Model):
    metrologyname=models.CharField(max_length=50)
    description=models.CharField(max_length=1000,blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)
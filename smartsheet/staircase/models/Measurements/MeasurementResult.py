from django.db import models
from django.utils import timezone
from .. import Foup

def add_raw_data_file(instance,filename):
    #define the location of the file to upload to
    return f'{instance.type}/{timezone.now().strftime("%Y-%m-%d")}/{filename}'

class MeasurementResult(models.Model):
    foup=models.ForeignKey(Foup, on_delete=models.SET_NULL,blank=True,null=True)
    datetime = models.DateTimeField(auto_now_add=True)  # creation time
    rawDataFile=models.FileField(upload_to=add_raw_data_file,null=True,blank=True)
    startingSlot=models.IntegerField()
    endingSlot=models.IntegerField()
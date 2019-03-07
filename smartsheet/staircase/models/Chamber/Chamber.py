from django.db import models
from django.utils import timezone
from .. import User,Group
from ..model_functions.add_configuration_file import add_configuration_file
import pandas as pd


class Chamber(models.Model):
    chamberName=models.CharField(max_length=30) #Chamber
    chamberPosition=models.CharField(max_length=30,null=True,blank=True) #eg: BayJ6
    timestamp=models.DateTimeField(auto_now_add=True)    #creation time
    note=models.CharField(max_length=200,null=True,blank=True)
    groups=models.ManyToManyField(Group,through='Chamber_Group_Relationship')
    def __str__(self):
        return self.chamberName

class Chamber_Group_Relationship(models.Model):
    chamber=models.ForeignKey(Chamber,on_delete=models.SET_NULL,null=True)
    group=models.ForeignKey(Group,on_delete=models.SET_NULL,null=True)
    start_date=models.DateField()
    end_date=models.DateField(null=True,blank=True)
    note=models.CharField(max_length=200,null=True,blank=True)


class Chamber_Configuration(models.Model):
    chamber=models.ForeignKey(Chamber,on_delete=models.SET_NULL,null=True)    #link to Chamber
    chamberDescription=models.CharField(max_length=10000,null=True,blank=True)
    #the following specifies the location of the raw configuration file to be uploaded to.
    descriptionFile=models.FileField(upload_to=add_configuration_file,null=True,blank=True)
    chamberOwner=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)    #creation time
    updated=models.DateTimeField(auto_now=True)  #update time
    note=models.CharField(max_length=200,null=True,blank=True)
    '''
    def save(self,*args,**kwargs):
        if not self.id:
            self.timestamp=timezone.now()
        self.updated=timezone.now()
        return super(Chamber, self).save(*args,**kwargs)
    '''
    def __str__(self):
        return self.chamber.chamberName+' / '+self.timestamp.strftime('%Y-%m-%d %H:%M')

    '''
    def generate_description(self):
        partlist=self.chamberpart_set.all()
        result='PartName,PartNumber,SerialNumber,Note'+'\n'
        for part in partlist:
            result=result+part.partName+','
            result=result+part.partNumber+','
            result=result+part.serialNumber+','
            result=result+part.note+'\n'
        self.chamberDescription=result
        return result

    def generate_parts(self,filename):
        # to generate a partlist from a .csv file. The csv file should contain 4 columns, which have "PartName","PartNumber","SerialNumber","Note" as the head rows respectively. The following rows contain the specific info for each part.
        partlist=[]
        data=pd.read_csv(filename)
        column_head=data.keys()
        length=len(data)
        for i in range(length):
            #first retreive the part info from the .csv file, then check whether the part is in chamberPart table
            iPartName=str(data[column_head[0]][i])
            iPartNumber=str(data[column_head[1]][i])
            iSerialNumber=str(data[column_head[2]][i])
            iNote=str(data[column_head[3]][i])
            #pdb.set_trace()
            search_existence=ChamberPart.objects.filter(partName=iPartName).filter(partNumber=iPartNumber).filter(serialNumber=iSerialNumber) #check whether the part exists in ChamberParts table
            if(len(search_existence)!=0):
                currentPart=search_existence[0]
                if currentPart.chamber==None:   #if the chamber part is in database but not linked to any chamber
                    partlist.append(currentPart)
                else:
                    last_chamber=Chamber.objects.filter(chamberName=self.chamberName).order_by('-configuretime')
                    if currentPart.chamber==last_chamber:   #if the found record for chamber part exist in the latest chamber record, just need to add the part record to partlist for the new chamber configuration
                        partlist.append(currentPart)
                    else:
                        print('The part: '+iPartName+'\t'+'PartNumber: '+iPartNumber+'\t'+'SerialNumber: '+iSerialNumber+'\t'+'is on Chamber: '+str(currentPart.chamber.chamberName))
                        return
            else:   #if the part is not in database
                new_part=ChamberPart(partName=str(data[column_head[0]][i]),partNumber=str(data[column_head[1]][i]),serialNumber=str(data[column_head[2]][i]),note=str(data[column_head[3]][i]))
                new_part.save()
                partlist.append(new_part)
        for part in partlist:
            part.chamber=self
            part.save()
        return partlist
'''
'''
class ChamberPart(models.Model):
    partName=models.CharField(max_length=30)
    chamber=models.ForeignKey(Chamber_Configuration,on_delete=models.SET_NULL,blank=True,null=True)
    partNumber=models.CharField(max_length=50,blank=True,null=True)
    serialNumber=models.CharField(max_length=50,blank=True,null=True)
    note=models.CharField(max_length=200,blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)    #creation time
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)  #update time
    def __str__(self):
        return self.partName+' / '+self.partNumber+' / '+self.serialNumber+' / '+self.updated.strftime('%Y-%m-%d %H:%M')
'''
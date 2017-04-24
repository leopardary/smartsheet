from django.db import models

from ..User import User
import pandas as pd
from datetime import datetime

class Chamber(models.Model):
    chamberName=models.CharField(max_length=30) #Chamber+side, eg: GT7A_S1
    chamberPosition=models.CharField(max_length=30) #eg: BayJ6
    chamberDescription=models.CharField(max_length=10000)
    chamberOwner=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)    #creation time
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)  #update time
    note=models.CharField(max_length=200)

    def generate_description(self):
        partlist=self.chamberpart_set.all()
        result='PartName,PartNumber,SerialNumber,Note'+'\n'
        for part in partlist:
            result=result+part.PartName+','
            result=result+part.PartNumber+','
            result=result+part.SerialNumber+','
            result=result+part.Note+'\n'
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
            search_existence=ChamberPart.objects.filter(partname=iPartName).filter(partnumber=iPartName).filter(serialnumber=iSerialNumber) #check whether the part exists in ChamberParts table
            if(len(search_existence)!=0):
                currentPart=search_existence[0]
                if currentPart.chamber==None:   #if the chamber part is in database but not linked to any chamber
                    partlist.add(currentPart)
                else:
                    last_chamber=Chamber.objects.filter(chamberName=self.chamberName).order_by('-configuretime')
                    if currentPart.chamber==last_chamber:   #if the found record for chamber part exist in the latest chamber record, just need to add the part record to partlist for the new chamber configuration
                        partlist.append(currentPart)
                    else:
                        print 'The part: '+iPartName+'\t'+'PartNumber: '+iPartNumber+'\t'+'SerialNumber: '+iSerialNumber+'\t'+'is on Chamber: '+str(currentPart.chamber.ID)
                        return
            else:   #if the part is not in database
                new_part=ChamberPart(partName=str(data[column_head[0]][i]),partNumber=str(data[column_head[1]][i]),serialNumber=str(data[column_head[2]][i]),note=str(data[column_head[3]][i]))
                new_part.save()
                partlist.append(new_part)
        for part in partlist:
            part.Chamber=self
            part.save()
        return partlist

class ChamberPart(models.Model):
    partName=models.CharField(max_length=30)
    chamber=models.ForeignKey(Chamber,on_delete=models.SET_NULL,blank=True,null=True)
    partNumber=models.CharField(max_length=50,blank=True,null=True)
    serialNumber=models.CharField(max_length=50,blank=True,null=True)
    note=models.CharField(max_length=200,blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)    #creation time
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)  #update time


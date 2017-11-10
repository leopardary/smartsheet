from __future__ import unicode_literals
from django.utils.encoding import smart_unicode
from django.db import models
import pdb

from ..User import User


class Foup(models.Model):
    foupname=models.CharField(max_length=16, verbose_name='Foup Name',primary_key=True)
    note=models.CharField(max_length=200,null=True,blank=True)
    owner=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)    #creation time
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)  #update time
    def __str__(self):
        return self.foupname

    @classmethod
    def create(cls,foupname,note,owner):
        #for foup in cls.objects.all():
        foup=cls(foupname=foupname,note=note,owner=owner)
        foup.save()
        for i in range(1,26):
            foup_slot=foup.foup_slot_set.create(slot=i)
            foup_slot.save()

        return foup
    def delete(self):
        #delete a foup from database
        for foup_slot in self.foup_slot_set.all():
            if foup_slot.wafer!=None:
                foup_slot.wafer.isused='Used'
            foup_slot.delete()
        self.delete()
        return

    def show_slots(self):
        #show the 25 slots of the foup, whether it is vacant, whether the contained wafer is new or used
        for i in range(1,26):
            foup_slot=self.foup_slot_set.filter(slot=i)[0]
            if foup_slot.wafer==None:
                print self.foupname+'\t'+'S'+str(i)+'\t'+'Vacant'
            else:
                print self.foupname+'\t'+'S'+str(i)+'\t'+foup_slot.wafer.isused
        return

class Wafer(models.Model):
    waferType=(
        ('PT', 'Particle Grade Wafer'),
        ('LR', 'Low Res Particle Grade Wafer'),
        ('MC', 'Mechanical Grade Wafer'),
        ('ER', 'External Reclaimed Wafer'),
        ('IR', 'Internal Reclaimed Wafer'),
    )

    used_choices=(
        ('N','New'),
        ('U','Used'),
    )
    isUsed=models.CharField(max_length=10,choices=used_choices)

    wafertype=models.CharField(max_length=20,choices=waferType,default='Internal Reclaimed Wafer')
    note=models.CharField(max_length=200,null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)    #creation time
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)  #update time
    def __str__(self):
        return smart_unicode(self.wafertype+' '+self.isUsed)


class Foup_slot(models.Model):
    foup=models.ForeignKey(Foup,on_delete=models.CASCADE)
    wafer=models.OneToOneField(Wafer,on_delete=models.SET_NULL,blank=True,null=True)    #setting on_delete=models.SET_NULL, means at times of deleting a wafer instance, the system sets this field to NULL
    slot=models.IntegerField(default=0)
    note=models.CharField(max_length=200,null=True,blank=True)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)  #update time
    def __str__(self):
        foup_name=self.foup.foupname
        s=foup_name+' S'+str(self.slot)+'\t'
        status=''
        if self.wafer is None:
            status='Vacant'
        else:
            status='Occupied\t'+'Wafer:\t'+self.wafer.isUsed
        return s+status
    def load_new_wafers(self,wafer_type):
        #load wafer into the current foup_slot: 1. check whether this slot is vacant; 2. load new wafers
        if self.wafer!=None:
            print "Slot: "+str(self.slot)+" still has wafer. Load unsuccessfull."
            return
        new_wafer=Wafer(isUsed='New',wafertype=wafer_type,note=self.foup.foupname+' S'+str(self.slot))
        #pdb.set_trace()
        new_wafer.save()
        self.wafer=new_wafer
        self.save()
        print "Load sucessfully."
        return
    def reclaim_wafer(self):
        if self.wafer==None:
            print "Slot: "+str(self.slot)+" is vacant."
        else:
            self.wafer=None
            self.save()
            print "Reclaim successfully"
        return
    def has_wafer(self):
        return self.wafer!=None
    def wafer_used(self):
        if self.has_wafer():
            if self.wafer.isUsed=='New':
                return False
            else:
                return True
        else:
            return False
from ..ProcessRecipe import ProcessRecipe
from django.db import models

class StaircaseRecipe(ProcessRecipe):
    CHAMBER_SIDE=(
        ('S1','Side_1'),
        ('S2','Side_2'),
    )
    TUNER_MODE=(
        ('A','Automatic'),
        ('F','Fixed'),
    )
    chamber_side=models.CharField(max_length=2,choices=CHAMBER_SIDE,blank=True,null=True)
    FacePlate_temp=models.IntegerField(default=250,editable=True,blank=True,null=True)
    SlitValve_purge=models.IntegerField(default=100,editable=True,blank=True,null=True)
    Bottom_purge=models.IntegerField(default=100,editable=True,blank=True,null=True)
    ESC_Voltage=models.IntegerField(default=275,editable=True,blank=True,null=True)
    Bottom_tuner_mode=models.CharField(max_length=1,choices=TUNER_MODE,blank=True,null=True)
    Bottom_tuner_p1=models.FloatField(default=19.0,editable=True,blank=True,null=True)
    Bottom_tuner_p2=models.FloatField(editable=True,blank=True,null=True)
    Top_tuner_mode=models.CharField(max_length=1,choices=TUNER_MODE,blank=True,null=True)
    Top_tuner_p1=models.FloatField(editable=True,blank=True,null=True)
    Top_tuner_p2 = models.FloatField(editable=True, blank=True, null=True)
    DepTime=models.FloatField(editable=True,blank=True,null=True)
    Heater_temp=models.IntegerField(default=550,editable=True,blank=True,null=True)
    HFRF=models.IntegerField(editable=True,blank=True,null=True)
    LFRF=models.IntegerField(editable=True,blank=True,null=True)
    Pressure=models.FloatField(editable=True,blank=True,null=True)
    Spacing=models.IntegerField(editable=True,blank=True,null=True)
    DPC_direction=models.IntegerField(editable=True,blank=True,null=True)
    DPC_amplitude=models.IntegerField(editable=True,blank=True,null=True)
    class Meta:
        abstract=True

class Staircase_Ox(StaircaseRecipe):
    #inheritance from StaircaseRecipe. This class additionally contains the Ox process gases.
    TEOS=models.IntegerField(editable=True,blank=True,null=True)
    N2O=models.IntegerField(editable=True,blank=True,null=True)
    AR=models.IntegerField(editable=True,blank=True,null=True)
    He=models.IntegerField(editable=True,blank=True,null=True)

class Staircase_Nit(StaircaseRecipe):
    #inheritance from StaircaseRecipe. This class additionally contains the Nit process gases.
    SiH4=models.IntegerField(editable=True,blank=True,null=True)
    NH3=models.IntegerField(editable=True,blank=True,null=True)
    N2=models.IntegerField(editable=True,blank=True,null=True)
    AR=models.IntegerField(editable=True,blank=True,null=True)
    He = models.IntegerField(editable=True, blank=True, null=True)

class Staircase_Stack(ProcessRecipe):
    #stack recipe, containing 2 foreign keys linking to the corresponding Ox and Nit recipe
    Ox=models.ForeignKey(Staircase_Ox,on_delete=models.SET_NULL,blank=True,null=True)
    Nit=models.ForeignKey(Staircase_Nit,on_delete=models.SET_NULL,blank=True,null=True)


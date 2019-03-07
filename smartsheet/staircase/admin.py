from django.contrib import admin

# Register your models here.
from .models import Wafer,User,Group,Project,Foup,Foup_slot,Chamber,Chamber_Configuration,Chamber_Group_Relationship,Thickness,Metrology,Recipe,Staircase_Ox,Staircase_Nit,Staircase_Stack,Staircase_Ox_Split,Staircase_Nit_Split,Staircase_Stack_Split

admin.site.register(Wafer)
admin.site.register(User)
admin.site.register(Group)
admin.site.register(Staircase_Nit_Split)
admin.site.register(Staircase_Ox_Split)
admin.site.register(Staircase_Stack_Split)
admin.site.register(Project)
admin.site.register(Foup)
admin.site.register(Foup_slot)
admin.site.register(Staircase_Ox)
admin.site.register(Staircase_Nit)
admin.site.register(Staircase_Stack)
admin.site.register(Chamber)
admin.site.register(Chamber_Configuration)
admin.site.register(Chamber_Group_Relationship)
admin.site.register(Thickness)
admin.site.register(Metrology)
admin.site.register(Recipe)
#admin.site.register(ChamberPart)


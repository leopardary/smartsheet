from django.contrib import admin

# Register your models here.
from .models import Wafer,User,Group,Split,Project,Foup,Foup_slot,ProcessRecipe,Chamber,Thickness,Metrology,Recipe

admin.site.register(Wafer)
admin.site.register(User)
admin.site.register(Group)
admin.site.register(Split)
admin.site.register(Project)
admin.site.register(Foup)
admin.site.register(Foup_slot)
admin.site.register(ProcessRecipe)
admin.site.register(Chamber)
admin.site.register(Thickness)
admin.site.register(Metrology)
admin.site.register(Recipe)


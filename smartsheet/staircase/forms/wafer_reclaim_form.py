from django import forms
from ..models.Wafer_Management.Wafer_Management import Foup,Foup_slot,Wafer

class wafer_reclaim_form(forms.Form):
    def __init__(self,foupname,*args,**kwargs):
        super(wafer_reclaim_form,self).__init__(*args,**kwargs)
        foup=Foup.objects.filter(foupname=foupname)[0]
        slot_list=foup.foup_slot_set.all()
        self.fields['slots']=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=[(slot.id,slot.slot) for slot in slot_list])


from django import forms
from ..models.User.User import Group,User
from ..models.Wafer_Management.Wafer_Management import Foup,Foup_slot,Wafer

class Foup_form(forms.Form):
    foupname=forms.CharField(label='Foup Name', max_length=120,widget=forms.TextInput(attrs={'class':'form-control'})) #,required=False
    user_list=[(user.id,user.first_name+" "+user.last_name) for user in User.objects.filter(group__group_name='Staircase')]
    owner=forms.ChoiceField(label='Owner',widget=forms.Select(attrs={'class':'form-control'}),choices=user_list)
    note=forms.CharField(label='Note',max_length=120,widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
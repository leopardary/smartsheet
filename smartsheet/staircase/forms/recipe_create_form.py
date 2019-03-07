from django import forms
from ..models.Chamber import Chamber
from ..models import User

class Staircase_Ox_recipe_create_form(forms.Form):
    chamberName=forms.CharField(label='Chamber Name', max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}),initial='GT7A Side1') #,required=False
    chamberPosition=forms.CharField(label='Chamber Position', max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}),initial='B85 Mod3 Bay J3',required=False)
    user_list=[(user.id,user.first_name+" "+user.last_name) for user in User.objects.filter(group__group_name='Staircase')]
    owner=forms.ChoiceField(label='Chamber Owner',widget=forms.Select(attrs={'class':'form-control'}),choices=user_list)
    note=forms.CharField(label='Note',max_length=120,widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    chamberDescription=forms.FileField(label='Select the Description file',required=False)  #the file should be MS-DOS csv file, containing all 4 columns for all rows


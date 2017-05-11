from django import forms
from ..models.User.User import Group,User


class user_form(forms.Form):

    first_name=forms.CharField(label='First Name:', max_length=120,widget=forms.TextInput(attrs={'class':'form-control'})) #,required=False
    last_name=forms.CharField(label='Last Name:',max_length=120,widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(label='Email:',widget=forms.EmailInput(attrs={'class':'form-control'}),required=False)
    phonenumber=forms.CharField(label='Phone Number:', max_length=120,widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    group_list=[(group.id,group.group_name) for group in Group.objects.filter(group_name='Staircase')]
    group=forms.ChoiceField(label='Group',widget=forms.Select(attrs={'class':'form-control'}),choices=group_list)


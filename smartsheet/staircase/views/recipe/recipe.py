from ...models import ProcessRecipe,Chamber
from django.shortcuts import render
from ...models import Group
from django.http import HttpResponseRedirect


def Ox_recipe(request):
    '''
    staircase=Group.objects.filter(group_name='Staircase')
    user_list=User.objects.filter(group=staircase[0]);
    context={
        'user_list':user_list,
    }
    '''
    staircase = Group.objects.filter(group_name='Staircase')
    chamber_list = Chamber.objects.filter(chamberOwner__group=staircase[0]);
    context = {
        'chamber_list': chamber_list,
    }
    return render(request,'staircase/recipe/recipe.html',context)

def Nit_recipe(request):
    '''
    staircase=Group.objects.filter(group_name='Staircase')
    user_list=User.objects.filter(group=staircase[0]);
    context={
        'user_list':user_list,
    }
    '''
    return render(request,'staircase/recipe/recipe.html')

def Stack_recipe(request):
    '''
    staircase=Group.objects.filter(group_name='Staircase')
    user_list=User.objects.filter(group=staircase[0]);
    context={
        'user_list':user_list,
    }
    '''
    return render(request,'staircase/recipe/recipe.html')
'''
def create_recipe(request):
    return render(request, 'staircase/recipe/create_recipe.html')
'''
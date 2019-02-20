from ...models import ProcessRecipe,Chamber
from django.shortcuts import render
from django.http import HttpResponseRedirect


def recipe(request):
    '''
    staircase=Group.objects.filter(group_name='Staircase')
    user_list=User.objects.filter(group=staircase[0]);
    context={
        'user_list':user_list,
    }
    '''
    return render(request,'staircase/recipe/recipe.html')

def create_recipe(request):
    return render(request, 'staircase/recipe/create_recipe.html')
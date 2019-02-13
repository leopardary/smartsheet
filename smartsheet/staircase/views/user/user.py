from ...models import Group, User
from ...forms import user_form
from django.shortcuts import render
from django.http import HttpResponseRedirect


def user(request):
    staircase=Group.objects.filter(group_name='Staircase')
    user_list=User.objects.filter(group=staircase[0]);
    context={
        'user_list':user_list,
    }
    return render(request,'staircase/user.html',context)
    #return HttpResponse("Here is managing users.")

def create_user(request):
    #return HttpResponse("Here is the page for creating users.")
    if request.method=='POST':
        form=user_form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/staircase/user/create')
    else:
        form=user_form()

    staircase=Group.objects.filter(group_name='Staircase')
    group_list=staircase;
    user_list=User.objects.filter(group=staircase[0]);
    context={
        'group_list':group_list,
        'user_list':user_list,
        'form':form,
    }
    return render(request,'staircase/create_user.html',context)



def save_user(request):
    if request.method=='POST':
        form=user_form(request.POST)
        if form.is_valid():
            User.create(first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],email=form.cleaned_data['email'],\
            phonenumber=form.cleaned_data['phonenumber'],group=form.cleaned_data['group'])
            return HttpResponseRedirect('/staircase/user/create')
    else:
        form=user_form()
    return render(request,'staircase/create_user.html',{'form':form})
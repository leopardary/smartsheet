from ...models import Group,Foup
from ...forms import Foup_form
from django.shortcuts import render
from django.http import HttpResponseRedirect

def foups(request):
    #foup_list=Foup.objects.all()
    #template=loader.get_template()
    staircase=Group.objects.filter(group_name='Staircase')
    foup_list=Foup.objects.filter(owner__group=staircase[0]);
    context={
        'foup_list':foup_list,
    }
    return render(request,'staircase/foup_wafer/foup_wafer.html',context)
    #return HttpResponse("Here is for managing foups and wafers.")

def create_foup(request):
    if request.method=='POST':
        form=Foup_form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/staircase/foups/create')
    else:
        form=Foup_form()

    staircase=Group.objects.filter(group_name='Staircase')
    group_list=staircase;
    foup_list=Foup.objects.filter(owner__group=staircase[0]);
    context={
        'group_list':group_list,
        'foup_list':foup_list,
        'form':form,
    }
    return render(request,'staircase/foup_wafer/create_foup.html',context)

def save_foup(request):
    if request.method=='POST':
        form=Foup_form(request.POST)
        if form.is_valid():
            Foup.create(foupname=form.cleaned_data['foupname'],note=form.cleaned_data['note'],owner=User.objects.filter(pk=form.cleaned_data['owner'])[0])
            return HttpResponseRedirect('/staircase/foups/create')
    else:
        form=Foup_form()
    return render(request,'staircase/create_foup.html',{'form':form})

def foup_detail(request,foup_name):
    staircase=Group.objects.filter(group_name='Staircase')
    foup_list=Foup.objects.filter(owner__group=staircase[0])
    foup=Foup.objects.filter(foupname=foup_name)[0]
    slot_list=foup.foup_slot_set.all()
    context={
    'foup':foup,
    'slot_list':slot_list,
	'foup_list':foup_list,
    }
    return render(request,'staircase/foup_wafer/foup_details/foup_detail.html',context)

from ...models import Group,Foup
from django.shortcuts import render
from django.http import HttpResponseRedirect

def reclaim_wafers(request,foup_name):
    staircase=Group.objects.filter(group_name='Staircase')
    foup_list=Foup.objects.filter(owner__group=staircase[0])
    foup=Foup.objects.filter(foupname=foup_name)[0]
    slot_list=foup.foup_slot_set.all()
    context={
    'foup':foup,
    'slot_list':slot_list,
	'foup_list':foup_list,
    }
    return render(request,'staircase/foup_wafer/foup_details/reclaim_wafers.html',context)

def reclaim_execute(request,foup_name):
    if request.method=='POST':
        staircase=Group.objects.filter(group_name='Staircase')
        foup_list=Foup.objects.filter(owner__group=staircase[0])
        foup=Foup.objects.filter(foupname=foup_name)[0]
        slot_list=request.POST.getlist('occupied_slot')
        #pdb.set_trace()
        for slot in slot_list:
            foup_slot=foup.foup_slot_set.filter(slot=int(slot))[0]
            foup_slot.reclaim_wafer()
        return HttpResponseRedirect('/staircase/foups/%s'%foup.foupname)
    return render(request,'/staircase/foups/%s'%foup.foupname)

def load_execute(request,foup_name):
    if request.method=='POST':
        staircase=Group.objects.filter(group_name='Staircase')
        foup_list=Foup.objects.filter(owner__group=staircase[0])
        foup=Foup.objects.filter(foupname=foup_name)[0]
        wafer_type=request.POST['wafer_type']
        slot_list=request.POST.getlist('available_slot')
        #pdb.set_trace()
        for slot in slot_list:

            foup_slot=foup.foup_slot_set.filter(slot=int(slot))[0]
            foup_slot.load_new_wafers(str(wafer_type))
        return HttpResponseRedirect('/staircase/foups/%s'%foup.foupname)
    return render(request,'/staircase/foups/%s'%foup.foupname)



def load_wafers(request,foup_name):
    staircase=Group.objects.filter(group_name='Staircase')
    foup_list=Foup.objects.filter(owner__group=staircase[0])
    foup=Foup.objects.filter(foupname=foup_name)[0]
    slot_list=foup.foup_slot_set.all()
    context={
    'foup':foup,
    'slot_list':slot_list,
	'foup_list':foup_list,
    }
    return render(request,'staircase/foup_wafer/foup_details/load_wafers.html',context)
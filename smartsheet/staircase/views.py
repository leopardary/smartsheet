from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Wafer, Foup, Foup_slot
from .models import User, Group
from django.template import loader
from .forms import user_form,Foup_form, wafer_reclaim_form, chamber_form
from .models import Chamber
import pdb

def index(request):
    return render(request,'staircase/index.html')
        #return HttpResponse("Hello, world. You're at the staircase homepage.")

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

def chamber(request):
    staircase=Group.objects.filter(group_name='Staircase')
    group_list=staircase
    chamber_list=Chamber.objects.filter(chamberOwner__group=staircase[0])
    context={
        'group_list':group_list,
        'chamber_list':chamber_list,
    }
    #return render(request,'staircase/create_chamber.html',context)
    return render(request,'staircase/chamber/chamber.html',context)
    #return HttpResponse("Here is managing the Chamber HW.")

def create_chamber(request):
    '''
    if request.method=='POST':
        form=chamber_form(request.POST,request.FILES)
        if form.is_valid():
            chamber=Chamber(chamberName=request.POST['chamberName'],chamberPosition=request.POST['chamberPosition'],descriptionFile=request.FILES['chamberDescription'],chamberOwner=request.POST['owner'],note=request.POST['note'])
            chamber.generate_parts(chamber.descriptionFile)
            chamber.chamberDescription=chamber.generate_description()
            chamber.save()
            return HttpResponseRedirect('/staircase/chamber')
    else:
        '''
    #pdb.set_trace()
    if request.method=='POST':
        form=chamber_form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/staircase/chamber/create')
    else:
        form=chamber_form()
    staircase=Group.objects.filter(group_name='Staircase')
    group_list=staircase
    chamber_list=Chamber.objects.filter(chamberOwner__group=staircase[0])
    context={
        'group_list':group_list,
        'chamber_list':chamber_list,
        'form':form,
    }
    return render(request,'staircase/chamber/create_chamber.html',context)

def save_chamber(request):
    #pdb.set_trace()
    if request.method=='POST':
        form=chamber_form(request.POST)
        if form.is_valid():
            owner=User.objects.filter(pk=int(request.POST['owner']))[0]
            chamber=Chamber(chamberName=request.POST['chamberName'],chamberPosition=request.POST['chamberPosition'],descriptionFile=request.FILES['chamberDescription'],chamberOwner=owner,note=request.POST['note'])
            #pdb.set_trace()
            chamber.save()
            chamber.generate_parts(chamber.descriptionFile.file)
            chamber.chamberDescription=chamber.generate_description()
            chamber.save()
            return HttpResponseRedirect('/staircase/chamber')
    else:
        form=chamber_form()
    return render(request,'staircase/create_chamber.html',{'form':form})

def chamber_detail(request,chamber_id):
    staircase=Group.objects.filter(group_name='Staircase')
    group_list=staircase
    chamber_list=Chamber.objects.filter(chamberOwner__group=staircase[0])
    chamber=Chamber.objects.filter(id=chamber_id)[0]
    #pdb.set_trace()
    part_list=chamber.chamberpart_set.all()
    context={
    'chamber':chamber,
    'part_list':part_list,
    'chamber_list':chamber_list,
    }
    return render(request,'staircase/chamber/chamber_detail.html',context)

def chamber_update(request,chamber_id):
    staircase=Group.objects.filter(group_name='Staircase')
    group_list=staircase
    chamber_list=Chamber.objects.filter(chamberOwner__group=staircase[0])
    chamber=Chamber.objects.filter(id=chamber_id)[0]
    part_list=chamber.chamberpart_set.all()
    context={
    'chamber':chamber,
    'part_list':part_list,
    'chamber_list':chamber_list,
    }
    return render(request,'staircase/chamber_update.html',context)

def chamber_delete(request,chamber_id):
    staircase=Group.objects.filter(group_name='Staircase')
    group_list=staircase
    chamber_list=Chamber.objects.filter(chamberOwner__group=staircase[0])
    chamber=Chamber.objects.get(id=chamber_id)
    chamber.delete()
    context={
    'chamber_list':chamber_list,
    }
    return render(request,'staircase/chamber/chamber.html',context)

def save_foup(request):
    if request.method=='POST':
        form=Foup_form(request.POST)
        if form.is_valid():
            Foup.create(foupname=form.cleaned_data['foupname'],note=form.cleaned_data['note'],owner=User.objects.filter(pk=form.cleaned_data['owner'])[0])
            return HttpResponseRedirect('/staircase/foups/create')
    else:
        form=Foup_form()
    return render(request,'staircase/create_foup.html',{'form':form})

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


def project(request):
    return render(request,'staircase/project.html')
    #return HttpResponse("Here is managing projects.")

def split(request):
    return HttpResponse("Here is managing splits.")

def user(request):
    staircase=Group.objects.filter(group_name='Staircase')
    user_list=User.objects.filter(group=staircase[0]);
    context={
        'user_list':user_list,
    }
    return render(request,'staircase/user.html',context)
    #return HttpResponse("Here is managing users.")



def measurementResult(request):
    return HttpResponse("Here is the measurement Result.")

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
##def user_fouplist(request,user):
##      try:
##        user1=User.objects.get()
# Create your views here.


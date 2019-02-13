from ...models import User, Group, Chamber
from ...forms import chamber_form
from django.shortcuts import render
from django.http import HttpResponseRedirect

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

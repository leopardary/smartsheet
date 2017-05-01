from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models.Wafer_Management.Wafer_Management import Wafer,Foup,Foup_slot
from .models.User.User import User,Group
from django.template import loader
from .forms import user_form

def index(request):
    return render(request,'staircase/index.html')
	#return HttpResponse("Hello, world. You're at the staircase homepage.")

def foups(request):
    #foup_list=Foup.objects.all()
    #template=loader.get_template()
	return render(request,'staircase/foup_wafer.html')
    #return HttpResponse("Here is for managing foups and wafers.")

def project(request):
    return render(request,'staircase/project.html')
    #return HttpResponse("Here is managing projects.")

def split(request):
    return HttpResponse("Here is managing splits.")

def user(request):
    return render(request,'staircase/user.html')
    #return HttpResponse("Here is managing users.")

def chamber(request):
    return render(request,'staircase/chamber.html')
    #return HttpResponse("Here is managing the Chamber HW.")

def measurementResult(request):
    return HttpResponse("Here is the measurement Result.")

def create_user(request):
    #return HttpResponse("Here is the page for creating users.")
    if request.method=='POST':
        form=user_form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form=user_form()
    return render(request,'staircase/create_user.html',{'form':form})


##def user_fouplist(request,user):
##	try:
##        user1=User.objects.get()
# Create your views here.

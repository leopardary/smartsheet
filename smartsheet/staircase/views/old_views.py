from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from ..models import Wafer, Foup, Foup_slot
from ..models import User, Group
from django.template import loader
from ..forms import user_form,Foup_form, wafer_reclaim_form, chamber_form
from ..models import Chamber
import pdb

def index(request):
    return render(request,'staircase/index.html')
        #return HttpResponse("Hello, world. You're at the staircase homepage.")

def project(request):
    return render(request,'staircase/project.html')
    #return HttpResponse("Here is managing projects.")

def split(request):
    return HttpResponse("Here is managing splits.")

def measurementResult(request):
    return HttpResponse("Here is the measurement Result.")


##def user_fouplist(request,user):
##      try:
##        user1=User.objects.get()
# Create your views here.

def thickness(request):
    return render(request,'staircase/thickness/thickness.html')
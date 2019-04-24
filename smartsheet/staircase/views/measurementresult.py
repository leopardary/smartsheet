from ..models import MeasurementResult
from django.shortcuts import render
from ..models import Foup
from django.http import HttpResponseRedirect

def measurementresult(request):
    foup_list=Foup.objects.all();
    context={
        'foup_list':foup_list,
    }
    return render(request,'staircase/measurementresult.html',context);

def measurementresultsave(request):
    return 0;
from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def home(request):
    context = {
        'data' : models.Quote.objects.all(),
    }
    return render(request, ('phys/phys_home.html'), context=context)

def bsc(request):
    context = {
        'data' : models.QuoteBSC.objects.all(),
    }
    return render(request, ('phys/Bsc.html'), context=context)

def msc(request):
    context = {
        'data' : models.QuoteMSC.objects.all(),
    }
    return render(request, ('phys/msc.html'), context=context)
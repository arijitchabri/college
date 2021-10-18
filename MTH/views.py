from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def admission(request):
    context = {
        'data' : models.Quote.objects.all(),
    }
    return render(request, ('mth/mth.html'), context=context)
def msc(request):
    context = {
        'data' : models.QuoteMSC.objects.all(),
    }
    return render(request, ('mth/msc.html'), context=context)
def bsc(request):
    context = {
        'data' : models.QuoteBSC.objects.all(),
    }
    return render(request, ('mth/bsc.html'), context=context)
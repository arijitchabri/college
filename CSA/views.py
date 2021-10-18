from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def admission(request):
    context = {
        'data' : models.Quote.objects.all(),
    }
    return render(request, ('csa/csa.html'), context=context)
def msc(request):
    context = {
        'data' : models.QuoteMSC.objects.all(),
    }
    return render(request, ('csa/msc.html'), context=context)
def bsc(request):
    context = {
        'data' : models.QuoteBSC.objects.all(),
    }
    return render(request, ('csa/bsc.html'), context=context)
def bca(request):
    context = {
        'data' : models.QuoteBCA.objects.all(),
    }
    return render(request, ('csa/bca.html'), context=context)

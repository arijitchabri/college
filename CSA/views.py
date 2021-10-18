from django.shortcuts import render
from django.http import HttpResponse
from .models import Quote

# Create your views here.
def admission(request):
    context = {
        'data' : Quote.objects.all(),
    }
    return render(request, ('csa/csa.html'), context=context)
def msc(request):
    return render(request, ('csa/msc.html'))
def bsc(request):
    return render(request, ('csa/bsc.html'))
def bca(request):
    return render(request, ('csa/bca.html'))

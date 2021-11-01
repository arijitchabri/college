from django.shortcuts import render
from django.http import HttpResponse
from common.models import Quote, Department, SubDepartment

# Create your views here.
def admission(request):

    scope = Department.objects.get(name = 'Math')
    scope2 = SubDepartment.objects.get(subDep = 'Home')
    

    context = {
        'data' : Quote.objects.filter(tag = scope).filter(tag2 = scope2),
    }

    return render(request, ('mth/mth.html'), context = context)
def msc(request):
    scope = Department.objects.get(name = 'Math')
    scope2 = SubDepartment.objects.get(subDep = 'M.Sc')
    

    context = {
        'data' : Quote.objects.filter(tag = scope).filter(tag2 = scope2),
    }

    return render(request, ('mth/msc.html'), context = context)
    
def bsc(request):
    scope = Department.objects.get(name = 'Math')
    scope2 = SubDepartment.objects.get(subDep = 'B.Sc')
    

    context = {
        'data' : Quote.objects.filter(tag = scope).filter(tag2 = scope2),
    }

    return render(request, ('mth/bsc.html'), context = context)
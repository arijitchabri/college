from django.shortcuts import render
from django.http import HttpResponse
from common.models import Quote, Department, SubDepartment

# Create your views here.
def home(request):

    scope = Department.objects.get(name = 'Physics')
    scope2 = SubDepartment.objects.get(subDep = 'Home')
    

    context = {
        'data' : Quote.objects.filter(tag = scope).filter(tag2 = scope2),
    }

    return render(request, ('phys/phys_home.html'), context = context)
def msc(request):
    scope = Department.objects.get(name = 'Physics')
    scope2 = SubDepartment.objects.get(subDep = 'M.Sc')
    

    context = {
        'data' : Quote.objects.filter(tag = scope).filter(tag2 = scope2),
    }

    return render(request, ('phys/msc.html'), context = context)
    
def bsc(request):
    scope = Department.objects.get(name = 'Physics')
    scope2 = SubDepartment.objects.get(subDep = 'B.Sc')
    

    context = {
        'data' : Quote.objects.filter(tag = scope).filter(tag2 = scope2),
    }

    return render(request, ('phys/Bsc.html'), context = context)
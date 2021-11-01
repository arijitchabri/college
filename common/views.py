from django.shortcuts import render
from django.http import HttpResponse
from .models import Quote, Department


# Create your views here.
def index (request):
    scope = Department.objects.get(name = 'Common')

    context = {
        
        'data' : Quote.objects.filter(tag = scope),
    }

    return render(request, 'college/home.html', context=context)
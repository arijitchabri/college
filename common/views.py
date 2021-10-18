from django.shortcuts import render
from django.http import HttpResponse
from .models import Quote
import datetime


# Create your views here.
def index (request):
    context = {
        'data' : Quote.objects.all(),
        'comment_date': datetime.date.today(),
    }
    return render(request, 'college/home.html', context = context)


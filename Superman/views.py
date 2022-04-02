from django.shortcuts import render
from django.http import HttpResponse
from .models import info

# Create your views here.
def skill(r):
    background = {'name': 'Clark Kent', 'city': 'Metropolis'}
    return render(r,'Superman/bio.html',context=background)

def supershow(r):
    data = info.objects.all()
    background = {'data':data}
    return render(r,'Superman/info.html',context=background)
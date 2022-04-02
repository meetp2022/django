from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def superhero(r):
    return render(r,'Superhero/Superhero.html')

@login_required
def comics(r):
    return render(r,'Superhero/Comics.html')

def login(r):
    return render(r,'registration/login.html')

def logout(r):
    return render(r,'Superhero/logout.html')
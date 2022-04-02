from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import infofeedback
# Create your views here.
def Batmanskill(r):
    background = {'Name':'Bruce Wayne', 'City': 'Gotham'}
    return render(r,'Batman/bio.html',context=background)

def show(r):
    form = infofeedback()
    my_dict = {'form': form}
    if r.method == 'POST':
        form = infofeedback(r.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data)
    return render(r, 'Batman/feedback.html', context=my_dict)

def base(r):
    return render(r,'Batman/home.html')

@login_required
def begins(r):
    return render(r,'Batman/begins.html')


def dark(r):
    return render(r,'Batman/darkknight.html')

def batcom(r):
    return render(r,'Batman/comics.html')


from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    about = About.objects.all()[0]
    context = {
        'about':about
    }

    return render(request,"index.html",context)


def about(request):
    about = About.objects.all()[0]
    context = {
        'about':about
    }

    return render(request,"about.html",context)
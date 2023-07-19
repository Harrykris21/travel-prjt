from django.http import HttpResponse
from django.shortcuts import render
# from models import Place
from .models import Place,Team


# Create your views here.

def demo(request):
    # return HttpResponse("Hello World")
    pl=Place.objects.all()
    tm= Team.objects.all()
    return render(request,"index.html",{'results':pl,'team':tm})

def about(request):
    return render(request,"about.html")
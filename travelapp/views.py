# from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
# def fun(request):
#     return HttpResponse("hello world")

from django.shortcuts import render
from . models import *
def home(request):
    obj=place.objects.all().order_by("-created_date")
    pack=Packages.objects.all().order_by('-create_date')
    test=Testimonials.objects.all()
    return render(request, 'index.html',{'results':obj,'package':pack,'test':test})


def destination(request):
    return render(request,'destination.html')

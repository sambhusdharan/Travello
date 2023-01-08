# from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
# def fun(request):
#     return HttpResponse("hello world")

from django.shortcuts import render
from . models import place
def fun(request):
    obj=place.objects.all
    # obj= place();
    # obj.name="kerala";
    # obj.desc="gods on country"
    # obj.price="100"

    return render(request, 'index.html',{'results':obj})


# def addition(request):
#     numb1=int(request.GET["num1"])
#     numb2 = int(request.GET["num2"])
#     numb3=numb1+numb2
#     return render(request,'result.html',{"valu":numb3})

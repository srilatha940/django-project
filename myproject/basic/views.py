from django.shortcuts import render
from django.http import HttpResponse  #getting http response through http request
from django.http import JsonResponse
# Create your views here.

def sample(request):       # created a sample function
    return HttpResponse("hello world")

def sample1(request):
    return HttpResponse("Welcome to django")

# def sampleInfo(request):
#     data={"name":"sri","city":"Hyd"}
#     return JsonResponse(data)

def sample2(request):
    # data=[1,2,3,4]
    data={"result":[1,2,3,4]}       # in json mostly we don't send data in the form of list we prefer dictionary 
    return JsonResponse(data,safe=False)

# def dynamicResponse(request):
#     name=request.GET.get("name","")
#     return HttpResponse(f"hello {name} how are you")

def addition(request):
    num1=request.GET.get("num1")
    num2=request.GET.get("num2")
    num1=int(num1)
    num2=int(num2)
    result=num1+num2
    return HttpResponse(f"Addition = {result}")

# def subtraction(request):
#     num1=request.GET.get("num1")
#     num2=request.GET.get("num2")
#     num1=int(num1)
#     num2=int(num2)
#     result=num1-num2
    # return HttpResponse(f"Subtraction = {result}")

# def multiplication(request):
#     num1=request.GET.get("num1")
#     num2=request.GET.get("num2")
#     num1=int(num1)
#     num2=int(num2)
#     result=num1*num2
#     return HttpResponse(f"Multiplication = {result}")

# def division(request):
#     num1=request.GET.get("num1")
#     num2=request.GET.get("num2")
#     num1=int(num1)
#     num2=int(num2)
#     result=num1/num2
#     return HttpResponse(f"Division = {result}")



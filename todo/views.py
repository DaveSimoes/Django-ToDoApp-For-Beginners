from django.http  import HttpResponse
from django.shortcuts import render


def addTask(request):
    print(request.POST)
    return HttpResponse('The form is submitted')
    
  
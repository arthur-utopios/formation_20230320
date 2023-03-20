from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request): 
    return HttpResponse("hello world")

def number(request, num):
    return HttpResponse(f"{num}")
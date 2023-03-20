from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request): 

    villes = ['paris', 'roubaix', 'toulouse']

    return render(request, 'blog/index.html', {'prenom': 'arthur', 'villes': villes})

def number(request, num):
    return HttpResponse(f"{num}")

def test_template(request):
    return render(request, 'base.html')
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Blog

# Create your views here.
def index(request): 

    villes = ['paris', 'roubaix', 'toulouse']

    return render(request, 'blog/index.html', {'prenom': 'arthur', 'villes': villes})

def number(request, num):
    return HttpResponse(f"{num}")

def test_template(request):
    b = Blog(name="mon blog", author="arthur")
    b.save()
    return HttpResponse("blog créé")

def get_all(request):
    """
    Retourne tous les blogs de la base de données
    """
    blogs = Blog.objects.all()
    return render(request, 'blog/blog-list.html', {'blogs': blogs})

def blog_detail(request, id: int):
    """
    Affiche le détail d'un blog
    """

    blog = get_object_or_404(Blog, pk=id)
    
    return render(request, 'blog/blog-detail.html', {'blog': blog})



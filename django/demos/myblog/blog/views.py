from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm
from .models import Blog, Comment
from django.views.generic import ListView, CreateView

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
    blog.comment = blog.comment_set.all()

    return render(request, 'blog/blog-detail.html', {'blog': blog})

class BlogListView(ListView):
    context_object_name = "blogs"
    model = Blog
    template_name = "blog/blog-list.html"


class BlogCreateView(CreateView):
    model = Blog
    fields = ['name', 'author']

def create_comment(request, blog_id: int):

    print(request.method)

    if request.method == 'GET':

        form = CommentForm()

        return render(request, 'blog/create-comment.html', {'form': form})

    if request.method == 'POST':
        
        blog = Blog.objects.get(pk=blog_id)

        comment = Comment(blog=blog)

        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            form.save()
        return redirect('blog:blog-detail', id=blog_id)

    raise Http404("Wrong http method")
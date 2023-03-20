from django.shortcuts import render

# Create your views here.

from django.views import generic
from .models import Blog, BlogAuthor, BlogComment
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.contrib.auth.models import User  # Blog author or commenter


def index(request):
    """
    Vue pour la page d'accueil
    """
    return render(
        request,
        'index.html',
    )


class BlogListView(generic.ListView):
    """
    Classe générique pour afficher les posts à l'aide d'une pagination
    """
    model = Blog
    paginate_by = 5


class BlogListByAuthorView(generic.ListView):
    """
    Classe générique pour afficher les posts d'un auteur
    """
    model = Blog
    paginate_by = 5
    template_name = 'blog/blog_list_by_author.html'

    def get_queryset(self):
        """
        Return une liste de post créé par un auteur en récupérant l'id dans l'URL
        """
        id = self.kwargs['pk']
        target_author = get_object_or_404(BlogAuthor, pk=id)
        return Blog.objects.filter(author=target_author)

    def get_context_data(self, **kwargs):
        """
        Ajout de l'auteur dans le context pour pouvoir l'afficher
        """
        # Appel de l'implémentation de la classe parent du context
        context = super(BlogListByAuthorView, self).get_context_data(**kwargs)
        # Récupération de l'auteur à l'aide du paramètre passé dans la requête
        context['blogger'] = get_object_or_404(BlogAuthor, pk=self.kwargs['pk'])
        return context


class BlogDetailView(generic.DetailView):
    """
    Classe générique pour voir le détail d'un post
    """
    model = Blog


class BloggerListView(generic.ListView):
    """
   Classe générique pour afficher les auteurs
    """
    model = BlogAuthor
    paginate_by = 5


class BlogCommentCreate(LoginRequiredMixin, CreateView):
    """
    Formulaire de création d'un commentaire avec connexion obligatoire
    """
    model = BlogComment
    fields = ['description', ]

    def get_context_data(self, **kwargs):
        """
        Ajouter le titre du blog associé dans le formulaire
        """
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        # Récupérer l'id du post et l'ajouter dans le context
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        """
        Ajouter l'auteur et le post avant validation du formulaire
        """
        # Récupération de l'utilisateur depuis la requête
        form.instance.author = self.request.user
        # Association du blog avec l'id passé en URL
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        # Appel de la méthod de la classe parente pour la validation du formulaire
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self):
        """
        Après validation du formulaire, redirection vers de détail du blog
        """
        return reverse('blog:blog-detail', kwargs={'pk': self.kwargs['pk'], })
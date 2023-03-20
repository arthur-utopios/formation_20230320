from django.db import models

# Create your models here.

from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User  # Importer la classe User de l'app Auth


class BlogAuthor(models.Model):
    """
    Représente un blogger
    """
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=400, help_text="Entrer votre biographie")

    class Meta:
        ordering = ["user", "bio"]

    def get_absolute_url(self):
        """
        Retourne les blogs d'un utilisateurs
        """
        return reverse('blog:blogs-by-author', args=[str(self.id)])

    def __str__(self):
        """
        Surcharge de la dunder string
        """
        return self.user.username


class Blog(models.Model):
    """
    Model représentant un post d'un utilisateur
    """
    name = models.CharField(max_length=200)
    # Ajout de la contrainte One-To-Many
    description = models.TextField(max_length=2000, help_text="Entrer une description")
    post_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)

    # Ajout du trie par défaut des entités
    class Meta:
        ordering = ["-post_date"]

    def get_absolute_url(self):
        """
        Retourne l'url d'un post précis
        """
        return reverse('blog:blog-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class BlogComment(models.Model):
    """
    Représente un commentaire sur un post
    """
    description = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    post_date = models.DateTimeField(auto_now_add=True)
    # Ajout des contraintes de clés étrangères
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        """
        Renvoie une description minifiée si la taille dépasse 75 caractères
        """
        len_title = 75
        if len(self.description) > len_title:
            titlestring = self.description[:len_title] + '...'
        else:
            titlestring = self.description
        return titlestring

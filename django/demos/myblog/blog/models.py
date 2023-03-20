from django.db import models

# Create your models here.

class Blog(models.Model):
    """
    représentation d'un blog
    """
    name = models.TextField(max_length=100, help_text="entrer le nom du blog")
    author = models.TextField(max_length=100, help_text="saisir le nom de l'auteur")
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:
        return self.name

class Comment(models.Model):
    """
    représentation d'une commentaire sur un blog
    """
    description = models.TextField(max_length=200, help_text="saisir le commentaire")
    posted_at = models.DateField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        ordering = ["posted_at"]

    def __str__(self) -> str:
        return self.description
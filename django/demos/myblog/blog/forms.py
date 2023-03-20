from django.forms import ModelForm
from .models import Comment

# Création d'un formulaire basé sur un modèle
class CommentForm(ModelForm):
    class Meta:
        # modèle à utiliser
        model = Comment
        # champs requis pour le formulaire
        fields = ['description']
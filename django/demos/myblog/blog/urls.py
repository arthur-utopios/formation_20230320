from django.urls import path
from . import views

# Variable qui permet la résolution d'URL dans les templates à l'aide du nom
app_name = 'blog'

urlpatterns = [
    # path prend en paramètre la route, une vue, et un nom (facultatif)
    path('', views.index, name="index"),
    # Utiliser des paramètres dans un URL
    path('<int:num>', views.number, name="number"),
    path('test', views.test_template, name="test"),
    path('blogs', views.get_all, name="blogs"),
    path('blogs/<int:id>', views.blog_detail, name="blog-detail"),
    path('blogs-generic', views.BlogListView.as_view()),
    path('blogs/create', views.BlogCreateView.as_view(), name="blog-create"),
    path('blogs/<int:blog_id>/comments/create', views.create_comment, name="create-comment")
]
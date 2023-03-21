from django.urls import path

from . import views
from django.views.decorators.cache import cache_page

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blogger/<int:pk>', views.BlogListByAuthorView.as_view(), name='blogs-by-author'),
    path('blog/<int:pk>', cache_page(60 * 2)(views.BlogDetailView.as_view()), name='blog-detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blog/<int:pk>/comment/', views.BlogCommentCreate.as_view(), name='blog-comment'),
    path('blog-test/<int:id>', views.get_blog_and_author, name='blog-test'),
]
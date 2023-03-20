from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # path prend en paramètre la route, une vue, et un nom (facultatif)
    path('', views.index, name="index"),
    path('<int:num>', views.number, name="number"),
    path('test', views.test_template, name="test"),
]
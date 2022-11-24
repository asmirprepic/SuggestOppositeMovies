from django.urls import path
from .views import index, search_movie


urlpatterns = [
    path('', index, name='index'),
    path('searchmovie',search_movie,name='searchmovie'),
]
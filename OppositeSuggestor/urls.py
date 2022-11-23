from django.urls import path
from OppositeSuggestor import views

urlpatterns = [
    path('', views.index, name='index'),
    path('searchmovie',views.search_movie,name='searchmovie'),
]
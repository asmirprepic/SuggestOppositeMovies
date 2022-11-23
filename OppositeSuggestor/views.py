from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Movies
import json
import urllib.request

import numpy as np
import pandas as pd
import seaborn as sns
import time
from .compute import Compute

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
# import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords


from MoviesCode.Code.DataHandlerCollab import DataHandlerCollab
from MoviesCode.Code.Recommender import Recommender
from django.views.decorators.csrf import csrf_protect

dataHand = DataHandlerCollab()
dataHand.loadCleandData()


# Create your views here.


def index(request): 

    movies = ''
    print(request.method)

    if request.method=='POST':
        print('Called Here')
        Movie=request.POST['Movie']
        
    else:
        Movie = ''
    

   
    if Movie != '':

        try:
        
            print('Starting Extraction')
            print(Movie)
            
            print(Compute.compute(dataHand.getMovies(),Movie,100,90))
            movies = (Compute.compute(dataHand.getMovies(),Movie,100,90)['title'])
           
            

            print('Finished')

        except:
            print('Something went wrong')
            

   
    print('Printing Movie')
    print(Movie)
    return render(request,'index.html',{'movies':movies,'Movie':Movie})

# /search 
def search_movie(request):
    
    if 'term' in request.GET:
        qs = Movies.objects.filter(movie_title__istartswith=request.GET.get('term')).order_by("movie_title")[:10]
        titles = list()

        for movie in qs:
            titles.append(movie.movie_title)
        
        return JsonResponse(titles,safe=False)
    
    return render(request,'index.html')


def simple_function(request):
    pass

def request_Movies(request):

    return None
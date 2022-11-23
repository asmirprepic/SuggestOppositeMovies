
import numpy as np
import pandas as pd
import seaborn as sns
import time

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
# import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords


from MoviesCode.Code.DataHandlerCollab import DataHandlerCollab
from MoviesCode.Code.Recommender import Recommender

class Compute:

    def __init__(self):
        pass

    def compute(movies,movie,nr_features,nr_components):

        # dataHand = DataHandlerCollab()
        # dataHand.loadCleandData()
        
        print('Testing Recommendation')
        recommender = Recommender(movies)
        print('Recommender instance success testing getRec...')
        recommendation = recommender.getRecommendation(movie,5,nr_features,nr_components )
       

        return (recommendation )

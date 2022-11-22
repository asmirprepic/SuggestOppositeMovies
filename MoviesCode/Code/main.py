
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


from DataHandlerCollab import DataHandlerCollab
from Recommender import Recommender

def main():
    dataHand = DataHandlerCollab()
    dataHand.loadCleandData()
    
    
    recommender = Recommender(dataHand.getMovies())
    recommender.getRecommendation('Toy Story',5 )
    
    

if __name__=="__main__":
    main()



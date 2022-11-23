import numpy as np
import pandas as pd
import seaborn as sns
import time

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
from nltk.corpus import stopwords

class Recommender:
    def __init__(self,df):
        self.df = df
        
    def createVectorizer(self,nr_features):
        print('Trying stop word')
        stop = list(stopwords.words('english'))
        print('Checking stop words')
        print(stop)
        
        print('Cheking tfdif')
        tfdif = TfidfVectorizer(max_features=nr_features,analyzer='word',stop_words=set(stop))
        print('Done checking tfdif')
        
        print('Vectorized_data printing')
        vectorized_data=tfdif.fit_transform(self.df['tags'])
        print(vectorized_data)
        print('Vectorized data done')
        
   
       
        return pd.DataFrame(vectorized_data.toarray(), index=self.df['tags'].index.tolist())
        

    def getSimilarity(self,movie_index,nr_features,nr_components):

      
        svd = TruncatedSVD(n_components=nr_components)
    
      
        reduced_data = svd.fit_transform(self.createVectorizer(nr_features))
        
        return cosine_similarity([reduced_data[movie_index,:]],reduced_data[0:,:])

    def getRecommendation(self,title,n,nr_features,nr_components):

        movie_index=self.df[self.df.title==title].new_id.values[0]
        print('Printing Movie Index')
        print(movie_index)


        cosine_sim = self.getSimilarity(movie_index,nr_features,nr_components)
        print('Printing Cosine sim')
        
        #sorted(list(enumerate(cosine_sim[movie_index])),key=lambda x: x[1],reverse=False)
       
        print('gettng scores')
        sim_score_all = sorted(list(enumerate(cosine_sim[0])),key=lambda x: x[1],reverse=False)
        
        

        if n>0:
            sim_score_all=sim_score_all[0:n]
        
    
        print('getting movie indecies')
        movie_indicies=[i[0] for i in sim_score_all]

        scores= [i[1] for i in sim_score_all]
        

        top_titles_df = pd.DataFrame(self.df.iloc[movie_indicies]['title'])
        top_titles_df['sim_scores'] = scores

        return(top_titles_df)







    
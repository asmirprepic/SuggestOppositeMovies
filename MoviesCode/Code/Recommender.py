import numpy as np
import pandas as pd
import seaborn as sns
import time


from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
from nltk.corpus import stopwords


class Recommender:
    def __init__(self, df):
        self.df = df
        self.reduced_data = None
        

    def createVectorizer(self, nr_features):

        stop = list(stopwords.words("english"))

        tfdif = TfidfVectorizer(
            max_features=nr_features, analyzer="word", stop_words=set(stop)
        )

        vectorized_data = tfdif.fit_transform(self.df["tags"])
        

        return pd.DataFrame(
            vectorized_data.toarray(), index=self.df["tags"].index.tolist()
        )
    
    def reduceData(self,nr_features,nr_components):
        svd = TruncatedSVD(n_components=nr_components)
        self.reduced_data=svd.fit_transform(self.createVectorizer(nr_features))

        return None

    def getSimilarity(self, movie_index):

        # svd = TruncatedSVD(n_components=nr_components)
        # reduced_data = svd.fit_transform(self.createVectorizer(nr_features)) 
        
    
        return cosine_similarity([self.reduced_data[movie_index, :]], self.reduced_data[0:, :])

    def getRecommendation(self, title, n):

        movie_index = self.df[self.df.title == title].new_id.values[0]
       

        cosine_sim = self.getSimilarity(movie_index)
        
        
        # sorted(list(enumerate(cosine_sim[movie_index])),key=lambda x: x[1],reverse=False)

        sim_score_all = sorted(
            list(enumerate(cosine_sim[0])), key=lambda x: x[1], reverse=False
        )

        if n > 0:
            sim_score_all = sim_score_all[0:n]

        movie_indicies = [i[0] for i in sim_score_all]

        scores = [i[1] for i in sim_score_all]

        top_titles_df = pd.DataFrame(self.df.iloc[movie_indicies]["title"])
        top_titles_df["sim_scores"] = scores

        return top_titles_df

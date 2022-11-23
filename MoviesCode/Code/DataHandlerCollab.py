import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import pathlib

class DataHandlerCollab:
    def __init__(self):
        self.df_meta = pd.DataFrame()
        self.df_credits = pd.DataFrame()
        self.df_keywords = pd.DataFrame()

        self.df_main = pd.DataFrame()
        self.df_movies = pd.DataFrame()


        pass

    def dataHandlerMain(self):
        self.dataLoader()
        self.dataLoadCleaner()
        self.dataCleaner()

    def dataLoader(self, path ='Data\\archive\\' ):
        DF_META_PATH = path + 'movies_metadata.csv'
        DF_CREDITS_PATH = path + 'credits.csv'
        DF_KEYWORDS_PATH = path + 'keywords.csv'
        
        
        self.df_meta = pd.read_csv(DF_META_PATH,low_memory = False, encoding = 'UTF-8')
        self.df_credits = pd.read_csv(DF_CREDITS_PATH, encoding = 'UTF-8')
        self.df_keywords = pd.read_csv(DF_KEYWORDS_PATH,low_memory = False, encoding = 'UTF-8')

        


    def dataLoadCleaner(self):
        self.df_meta=self.df_meta.drop([19730,29503,35587])
        
        self.df_meta = self.df_meta.set_index(self.df_meta['id'].str.strip().replace(',','').astype(int))
        
        
        self.df_credits = self.df_credits.set_index('id')
        
        self.df_keywords = self.df_keywords.set_index('id')


    def dataCleaner(self):
        df_temp = self.df_keywords.merge(self.df_credits, left_index = True,right_on = 'id')
       
  
       
        

        self.df_main = df_temp.merge(self.df_meta[['release_date','genres','overview','title']],left_index = True,right_on='id')

        del self.df_meta, self.df_keywords, self.df_credits, df_temp

       

        self.df_movies['keywords'] = self.df_main['keywords'].apply(lambda x: [i['name'] for i in eval(x)])
        self.df_movies['keywords'] = self.df_movies['keywords'].apply(lambda x: ' '.join([i.replace(" ","") for i in x]))
        

        self.df_movies['overview'] = self.df_main['overview'].fillna('')

        self.df_movies['release_date'] = pd.to_datetime(self.df_main['release_date'],errors='coerce').apply(lambda x:str(x).split('-')[0] if x != np.nan else np.nan)

        self.df_movies['cast'] = self.df_main['cast'].apply(lambda x: [i['name'] for i in eval(x)])
        self.df_movies['cast'] = self.df_movies['cast'].apply(lambda x: ' '.join([i.replace(" ","") for i in x]))

        self.df_movies['genres'] = self.df_main['genres'].apply(lambda x: [i['name'] for i in eval(x)])
        self.df_movies['genres'] = self.df_movies['genres'].apply(lambda x: ' '.join([i.replace(" ","") for i in x]))
        
        self.df_movies['title'] = self.df_main['title']

        self.df_movies['tags'] = self.df_movies['keywords'] + self.df_movies['cast'] + ' ' + self.df_movies['genres'] + ' ' +self.df_movies['release_date']


        self.df_movies.drop(self.df_movies[self.df_movies['tags']==''].index,inplace=True)
        self.df_movies.drop_duplicates(inplace=True)

        self.df_movies['new_id'] = range(0,len(self.df_movies))
        
        self.df_movies = self.df_movies[['new_id','title','tags']]

    def outputMovies(self):
        self.df_movies.to_csv('Opposite_Movies_Web\\MoviesCode\\Data\\output\\movies_output.csv')

    def getMovies(self):
        return self.df_movies

    def loadCleandData(self):
       
        self.df_movies = pd.read_csv(pathlib.Path(__file__).parent.parent / 'Data/movies_output.csv',low_memory = False, encoding = 'UTF-8')
        

        




    

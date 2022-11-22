import pandas as pd 


class DataHandler:

    def __init__(self):
        
        self.df =pd.DataFrame()
        self.pt = pd.DataFrame()


    def get_df(self):
        return self.df
    
    def set_df(self,df):
        self.df=df

    def set_pt(self,pt):
        self.pt = pt
    
    def get_pt(self):
        return self.pt

       

    def importData(self, datapath ="Data\\u.data"):
        df1 = pd.read_csv(datapath,sep='\t')
        df1.columns = ['user_id','item_id','rating','timestamp']
        df2  = pd.read_csv("Data\\Movie_Id_Titles")

        self.set_df(pd.merge(df1,df2,on='item_id'))
        
       

        del df1,df2

        

        

    def prepareData(self):
        
        rating_and_no_of_rating = pd.DataFrame(self.df.groupby('title')['rating'].mean().sort_values(ascending=False))
        rating_and_no_of_rating['no_of_ratings'] = self.df.groupby('title')['rating'].count()
        rating_and_no_of_rating = rating_and_no_of_rating.sort_values('no_of_ratings',ascending=False)
        
        self.set_pt(self.df.pivot_table(index='user_id',columns='title',values='rating'))
        
        return rating_and_no_of_rating


    def prediction(self):
        
        test_movie = input('Enter movie name -->')
        pt_temp = self.get_pt()
      
        movie_vector = pt_temp[test_movie]

        similar_movies = pt_temp.corrwith(movie_vector)
      
        
        corr_df = pd.DataFrame(similar_movies,columns=['Correlation'])
        corr_df = corr_df.join(self.prepareData()['no_of_ratings'])
        corr_df = corr_df[corr_df['no_of_ratings']>100].sort_values('Correlation',ascending=True).dropna()
        corr_df.head(10)

        print(corr_df.head(10))


      

        
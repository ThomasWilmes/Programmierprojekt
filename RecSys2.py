# To store the data
from warnings import catch_warnings
import pandas as pd

# To do linear algebra
import numpy as np

# To create interactive plots
from plotly.offline import init_notebook_mode
import plotly.graph_objs as go
init_notebook_mode(connected=True)
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

# Get Data
def RecSystem(id):
    new_Combined = 'C:/Users/passi/OneDrive - Hochschule Osnabrück/Semester 5-Veve/Programmierprojekt/Combined_Data_All.gzip'
    movie_tile_File = 'C:/Users/passi/OneDrive - Hochschule Osnabrück/Semester 5-Veve/Programmierprojekt/movie_titles.csv'

    data = pd.read_parquet(new_Combined)
    Convert_dic_data= {'Cust_Id': 'int64', 'Rating': 'float32', 'Movie_Id': 'Int64'}
    data= data.astype(Convert_dic_data)
    del new_Combined

    movie_titles = pd.read_csv(movie_tile_File,
                            encoding = "ISO-8859-1",
                            delimiter= '\t',
                            header = None,
                            names = ['Target'])
                            # Speicher alle Daten erst in eine Reihe, danach trennt er diese
    movie_titles[['Movie_Id', 'Year', 'Name']] = movie_titles['Target'].str.split(pat=",",n=2, expand=True)   
    movie_titles= movie_titles.drop(['Target', 'Year'], axis= 1)  
    Convert_dic= {'Movie_Id': 'int64', 'Name': 'str'}
    movie_titles = movie_titles.astype(Convert_dic)

    del Convert_dic

    ####################################################
    # Filter Data
    #
    df = data
    # Filter sparse movies
    min_movie_ratings = 1000
    filter_movies = (df['Movie_Id'].value_counts()>min_movie_ratings)
    filter_movies = filter_movies[filter_movies].index.tolist()

    # Filter sparse users
    min_user_ratings = 200
    filter_users = (df['Cust_Id'].value_counts()>min_user_ratings)
    filter_users = filter_users[filter_users].index.tolist()

    # Actual filtering
    df_filterd = df[(df['Movie_Id'].isin(filter_movies)) & (df['Cust_Id'].isin(filter_users))]
    del filter_movies, filter_users, min_movie_ratings, min_user_ratings, data, df


    # pivot and create movie-user matrix
    movie_user_mat = df_filterd.pivot(index='Movie_Id', columns='Cust_Id', values='Rating').fillna(0)
    
    user_movie_table_matrix = csr_matrix(movie_user_mat.values)
    model_knn = NearestNeighbors(metric = 'cosine', algorithm = 'auto',n_jobs=-1)
    model_knn.fit(user_movie_table_matrix)

    
    # Film wird ausgewählt!
    #query_index = id

    
    # Berechnen des Nächsten Nachbarn
    try:
        distances, indices = model_knn.kneighbors(movie_user_mat.loc[[id]].values.reshape(1,-1), n_neighbors = 120)
    except:
        return 0

    ## Ausgabe
    movie = []
    distance = []

    for i in range(0, len(distances.flatten())):
        if i != 0:
            movie.append(movie_user_mat.index[indices.flatten()[i]])
            distance.append(distances.flatten()[i])    

    m=pd.Series(movie,name='Movie_Id')
    d=pd.Series(distance,name='distance')
    recommend = pd.concat([m,d], axis=1)
    recommend = recommend.sort_values('distance',ascending=False)

    #print('Recommendations for {0}:\n'.format(movie_user_mat[id]))
    recMovies = recommend["Movie_Id"].iloc[range(0,5)]

    return recMovies

    ###
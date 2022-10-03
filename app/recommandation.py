import csv
import pandas as pd
# RecSys
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
  
import warnings
from app.KNN import find_similar_movies

from app.matrix import create_matrix
warnings.simplefilter(action='ignore', category=FutureWarning)
movies = pd.read_csv("../data/movie_titles_new.csv", encoding = "ISO-8859-1")
ratings = pd.read_csv("../data/Combined_dat_new_final.csv", encoding = "ISO-8859-1")
  
X, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper = create_matrix(ratings)
# end RecSys

listOfMovies = []
listOfRecommendations = []

def parseCSV(filePath):
      # CVS Column Names
      col_names = ['id','film']
      # Use Pandas to parse the CSV file
      csvData = pd.read_csv(filePath,names=col_names, header=None)
      # Loop through the Rows
      for i,row in csvData.iterrows():
             print(i,row['id'],row['film'],)

def getListOfMovies():
    global listOfMovies
    with open("data/movie_titles.csv", newline='', encoding='latin-1') as f:
        reader = csv.reader(f) 
        if not listOfMovies:          
            listOfMovies = list(reader)
        return listOfMovies


def getListOfRecommendations(id):
    movie_titles = dict(zip(movies['Id'], movies['Name']))
    
    movie_id = id
    
    similar_ids = find_similar_movies(movie_id, X, k=5)
    movie_title = movie_titles[movie_id]
    
    print(f"Since you watched {movie_title}")
    for i in similar_ids:
        print(movie_titles[i])

    return similar_ids


def getRecommendation():
    return None
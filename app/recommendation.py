#import csv
#import pandas as pd

from dataclasses import dataclass

listOfMovies = []
listOfRecommendations = []

@dataclass(unsafe_hash=True)
class Movie:
    id: int
    title: str

#def parseCSV(filePath):
      # CVS Column Names
#      col_names = ['id','film']
      # Use Pandas to parse the CSV file
#      csvData = pd.read_csv(filePath,names=col_names, header=None)
      # Loop through the Rows
#      for i,row in csvData.iterrows():
#            return (i,row['id'],row['film'],)

def getListOfMovies():
    global listOfMovies
    with open("data/movie_titles.csv", encoding='latin-1') as f:
        for line in f:
            listOfMovies.append(create_movie(line))
        return listOfMovies

def create_movie(line):
    movie = line.split(',')
    movie_id = movie[0]
    movie_title = movie[1]
    movie = movie[2:-1]
    if (movie.count('') < len(movie)):
        movie_title += ','.join(movie)
    return Movie(id=movie_id, title=movie_title)

def getListOfRecommendations(movies):
    return movies


def getRecommendation():
    return None

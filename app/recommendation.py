import csv
import pandas as pd
import json

from dataclasses import dataclass

movieList = []

@dataclass(unsafe_hash=True)
class Movie:
    title: str
    id: int


#def parseCSV(filePath):
      # CVS Column Names
#      col_names = ['id','film']
      # Use Pandas to parse the CSV file
#      csvData = pd.read_csv(filePath,names=col_names, header=None)
      # Loop through the Rows
#      for i,row in csvData.iterrows():
#            return (i,row['id'],row['film'],)

df = pd.read_csv("data/movie_titles.csv")

def parse_csv(df):
    res = df.to_json(orient="records")
    parsed = json.loads(res)
    return parsed

def getMovieList():
    global movieList
    with open("data/movie_titles.csv", encoding='latin-1') as f:
        for line in f:
            movieList.append(add_movie(line))
        return movieList

def add_movie(line):
    movie = line.split(',')
    movie_id = movie[0]
    movie_title = movie[1]
    movie = movie[2:-1]
    if (movie.count('') < len(movie)):
        movie_title += ','.join(movie)
    return Movie(id=movie_id, title=movie_title)

import csv
import pandas as pd


listOfMovies = []
listOfRecommendations = []

def parseCSV(filePath):
      # CVS Column Names
      col_names = ['id','film']
      # Use Pandas to parse the CSV file
      csvData = pd.read_csv(filePath,names=col_names, header=None)
      # Loop through the Rows
      for i,row in csvData.iterrows():
            return (i,row['id'],row['film'],)

def getListOfMovies():
    global listOfMovies
    with open("data/movie_titles.csv", newline='', encoding='latin-1') as f:
        reader = csv.reader(f) 
        if not listOfMovies:          
            listOfMovies = list(reader)
        return listOfMovies


def getListOfRecommendations(movies):
    return movies


def getRecommendation():
    return None

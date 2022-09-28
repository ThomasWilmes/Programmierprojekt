import csv

listOfMovies = []
listOfRecommendations = []


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

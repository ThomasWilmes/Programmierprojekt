'''The Recommendation System'''
import pandas as pd
from dataclasses import dataclass

movieList = []

@dataclass(unsafe_hash=True)
class Movie:
    '''Define a Movie'''
    title: str
    m_id: int

class Recommendation:
    movie_id: int
    recommendations: str


def get_movie_list() -> list[Movie]:
    '''Return a List of all Movies'''
    movieList: list[Movie] = []
    with open("data/movie_titles.csv", encoding='latin-1') as f:
        for eachLine in f:
             movieList.append(add_movie(eachLine))
        return  movieList


def get_recommendation_list() -> list[Recommendation]:
    '''Return a List of all Movies'''
    movieList: list[Recommendation] = []
    with open("data/Movie_Recommendations_comma.csv", encoding='latin-1') as f:
        for eachLine in f:
             movieList.append(add_recommendation(eachLine))
        return  movieList
   

def add_recommendation(line):
    '''add a recommendation to the List'''
    movie = line.split(',')
    movie[-1] = movie[-1].replace('\n', '')
    movie_id = movie.pop(0)
    if (len(movie) > 1):
        movie_title = movie.pop(0)
        movie_title += ','.join(movie)
    else:
        movie_title = movie[0]
    return Recommendation(movie_id=movie_id, recommendations=movie_title)

def add_movie(line):
    '''add a Movie to the List'''
    movie = line.split(',')
    movie[-1] = movie[-1].replace('\n', '')
    movie_id = movie.pop(0)
    if (len(movie) > 1):
        movie_title = movie.pop(0)
        movie_title += ','.join(movie)
    else:
        movie_title = movie[0]
    return Movie(m_id=movie_id, title=movie_title)

def get_list_of_recommendation(movies: list[int]) -> list[Recommendation]:
    movie_recommendations: list[Recommendation] = []
    for movie in movies:
        if (movie > 17770):
            raise ValueError('The given id is not an actual movie')
        df = pd.read_csv('data/Movie_Recommendations_comma.csv', header=None)
        recommendations = (df.loc[df[0] == movie].values).tolist()[0]
        movie_recommendations.append(Recommendation(
            movie_id=movie, recommendations=recommendations[1:5]))
    return movie_recommendations
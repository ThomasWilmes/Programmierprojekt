'''The Recommendation System'''
import pandas as pd
from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Movie:
    '''Define the Dataclass for a Movie'''
    title: str
    id: int
    release_year: str
    
@dataclass(unsafe_hash=True)
class Recommendation:
    '''Define the Dataclass for a Recommendation '''
    movie_id: int
    movie_title: str
    


    recommendations_ids: list[int]
    recommendations_titles:list[str]

def get_movie_list() -> list[Movie]:
    '''Return a List of all Movies'''
    movieList: list[Movie] = []
    with open("data/movie_titles.csv", encoding='latin-1') as f:
        for eachLine in f:
             movieList.append(create_movie(eachLine))
        return  movieList
   
def create_movie(line: str) -> Movie:
    """
    separates one movie at a time from the source file to insert it into a list
    """
    movie = line.split(',')
    movie[-1] = movie[-1].replace('\n', '')
    movie_id = movie.pop(0)
    movie_date = movie.pop(0)
    if (len(movie) > 1):
        movie_title = movie.pop(0)
        movie_title += ','.join(movie)
    else:
        movie_title = movie[0]
    return Movie(id=movie_id, release_year=movie_date, title=movie_title)



def get_list_of_recommendation(movies: list[int]) -> list[Recommendation]:
    """
    returns a list
    """
    movie_recommendations: list[Recommendation] = []
    for movie in movies:
        if (movie > 17770):
            raise ValueError('The given id is not an actual movie')

        df_titels = pd.read_csv('data/recommendations_titles.csv', header=None, sep=';')        
        df_ids = pd.read_csv('data/recommendations_ids.csv', header=None, sep=';')

        recommendations_titles = (df_titels.loc[df_titels[0] == movie].values).tolist()[0]       
        recommendations_ids = (df_ids.loc[df_ids[0] == movie].values).tolist()[0]

        movie_recommendations.append(Recommendation(
            movie_id=recommendations_ids[0], 
            movie_title=recommendations_titles[1],
            recommendations_ids=recommendations_ids[1:6], 
            recommendations_titles=recommendations_titles[2:7]))
    return movie_recommendations

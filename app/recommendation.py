'''The Recommendation System'''
from dataclasses import dataclass
import pandas as pd
import math


@dataclass(unsafe_hash=True)
class Movie:
    '''Define the Dataclass for a Movie'''
    title: str
    m_id: int
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
    movie_list: list[Movie] = []
    with open("data/movie_titles.csv", encoding='latin-1') as f:
        for each_line in f:
             movie_list.append(create_movie(each_line))
        return  movie_list
   
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
    return Movie(m_id=movie_id, release_year=movie_date, title=movie_title)






def get_recommendationcount_for_movieindex(index,anzahlgesamt) -> int:
    if index > 5:
        return 0
    x = 5 % anzahlgesamt
    y = math.floor(5/anzahlgesamt)
    return y+1 if index <= x else y
def get_list_of_recommendation(movies: list[int]) -> list:
    """
    returns a list
    """
    original_movies = []
    movie_recommendations = []
    for x,movie in enumerate(movies):
        if (movie > 17770):
            raise ValueError('The given id is not an actual movie')
        df_titels = pd.read_csv('data/recommendations_titles.csv', header=None, sep=';')        
        df_ids = pd.read_csv('data/recommendations_ids.csv', header=None, sep=';')
        recommendations_titles = (df_titels.loc[df_titels[0] == movie].values).tolist()[0]       
        #check fehlt aber noch :D
        recommendations_ids = (df_ids.loc[df_ids[0] == movie].values).tolist()[0]
        anzahl_recommendations = get_recommendationcount_for_movieindex(x+1,len(movies))        #wenn man über dem index 5 ist und somit keine filme mehr vorgeschlagen werden sollen wird direkt returned
        if anzahl_recommendations == 0:
            return movie_recommendations
        original_movies.append({
            "title":(df_titels.loc[df_titels[0] == movie].values).tolist()[0][1],
            "id":movie
        })    
        for (id,title) in zip(recommendations_ids[1:(1+anzahl_recommendations)],recommendations_titles[2:(2+anzahl_recommendations)]):
            movie_recommendations.append({
                "id":id,
                "title":title
            })
    return {
        "original_movies":original_movies,
        "recommendation":movie_recommendations
    }

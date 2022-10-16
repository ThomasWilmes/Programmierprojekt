'''The Recommendation System'''
import math
from dataclasses import dataclass

import pandas as pd


@dataclass(unsafe_hash=True)
class Movie:
    '''Define the Dataclass for a Movie'''
    title: str
    m_id: int
    release_year: str
    

def get_movie_list() -> list[Movie]:
    '''
    Return a List with ID, release year and title of all Movies
    '''
    movie_list: list[Movie] = []
    with open("data/movie_titles.csv", encoding='latin-1') as f:
        for each_line in f:
            movie_list.append(create_movie(each_line))
        return movie_list


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


def get_recommendationcount_for_movieindex(index, total) -> int:
    """
    Calculates how many recommendations will be displayed per input to get five recommendations in the end.
    """
    if index > 5:
        return 0
    x = 5 % total
    y = math.floor(5/total)
    return y+1 if index <= x else y


def get_list_of_recommendation(movies: list[int]) -> list:
    """
    Checks if the entered ID is greater than the number of movies. Loads the recommendations as IDs and titles from the .csv file. If there is a recommendation it will be sent together with the input values.
    """
    original_movies = []
    movie_recommendations = []
    for x, movie in enumerate(movies):
        if (movie > 17770):
            raise ValueError('The given id is not an actual movie')
        df_titels = pd.read_csv(
            'data/recommendations_titles.csv', header=None, sep=';')
        df_ids = pd.read_csv(
            'data/recommendations_ids.csv', header=None, sep=';')
        recommendations_titles = (
            df_titels.loc[df_titels[0] == movie].values).tolist()[0]
        recommendations_ids = (
            df_ids.loc[df_ids[0] == movie].values).tolist()[0]
        quantity_recomendations = get_recommendationcount_for_movieindex(
            x+1, len(movies))
        if quantity_recomendations == 0:
            return movie_recommendations
        original_movies.append({
            "title": (df_titels.loc[df_titels[0] == movie].values).tolist()[0][1],
            "id": movie
        })
        for (id, title) in zip(recommendations_ids[1:(1+quantity_recomendations)], recommendations_titles[2:(2+quantity_recomendations)]):
            movie_recommendations.append({
                "id": id,
                "title": title
            })
    return {
        "original_movies": original_movies,
        "recommendation": movie_recommendations
    }

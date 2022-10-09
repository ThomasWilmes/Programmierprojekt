'''The Recommendation System'''

from dataclasses import dataclass

movieList = []

@dataclass(unsafe_hash=True)
class Movie:
    '''Define a Movie'''
    title: str
    m_id: int



def get_movie_list() -> list[Movie]:
    '''Return a List of all Movies'''
    movieList: list[Movie] = []
    with open("data/movie_titles.csv", encoding='latin-1') as f:
        for eachLine in f:
             movieList.append(build_movie_list(eachLine))
        return  movieList
   


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
    
    

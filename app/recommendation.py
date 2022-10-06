'''The Recommendation System'''

from dataclasses import dataclass

movieList = []

@dataclass(unsafe_hash=True)
class Movie:
    '''Define a Movie'''
    title: str
    m_id: int


#def parseCSV(filePath):
      # CVS Column Names
#      col_names = ['id','film']
      # Use Pandas to parse the CSV file
#      csvData = pd.read_csv(filePath,names=col_names, header=None)
      # Loop through the Rows
#      for i,row in csvData.iterrows():
#            return (i,row['id'],row['film'],)

def get_movie_list():
    '''Return a List of all Movies'''
    global MOVIE_LIST
    with open("data/movie_titles.csv", encoding='latin-1') as f:
        for line in f:
            MOVIE_LIST.append(add_movie(line))
        return MOVIE_LIST

def add_movie(line):
    '''add a Movie to the List'''
    movie = line.split(',')
    movie_id = movie[0]
    movie_title = movie[1]
    movie = movie[2:-1]
    if movie.count('') < len(movie):
        movie_title += ','.join(movie)
    return Movie(m_id=movie_id, title=movie_title)

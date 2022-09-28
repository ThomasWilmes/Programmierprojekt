listOfMovies = []
listOfRecommendations = []

@app.route("/")
def hello_world():
    return "<p>Go to /movies for a List of Movies</p>"

def getListOfMovies():         
        listOfMovies = ["Film1", "Film2", "Film3", "Film4", "Film5"]
        return listOfMovies


def getListOfRecommendations(movies):
    return movies


def getRecommendation():
    return None

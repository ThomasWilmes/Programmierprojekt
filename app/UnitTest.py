from recommandation import get_list_of_recommendation

def test_RecSystemOutputFiveMovies():
    id = 3
    recommandedMovies = get_list_of_recommendation(id)

    if recommandedMovies.size == 5:
        print("Die es wird die richtige Anzahl an empfohlenden Filme zurückgegeben")
    else:
        print("test_RecSystemOutputFiveMovies failed")

def test_RecSystemOutputZeroWhenNoID():
    id = None
    recommandedMovies = get_list_of_recommendation(id)

    if recommandedMovies == 0:
        print("Es wird keine Liste zurückgegeben bei keiner ID")
    else:
        print("test_RecSystemOutputZeroWhenNoID failed")

def test_RecSystemOutputZeroWhenInvalidID():
    id = "Invalid"
    recommandedMovies = get_list_of_recommendation(id)

    if recommandedMovies == 0:
        print("Es wird keine Liste zurückgegeben bei invalider ID")
    else:
        print("test_RecSystemOutputZeroWhenInvalidID failed")

test_RecSystemOutputFiveMovies()
test_RecSystemOutputZeroWhenNoID()
test_RecSystemOutputZeroWhenInvalidID()
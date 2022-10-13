from RecSys2 import RecSystem

def test_RecSystemOutputFiveMovies():
    id = 3
    recommandedMovies = RecSystem(id)

    if recommandedMovies.size == 5:
        print("Die es wird die richtige Anzahl an empfohlenden Filme zurückgegeben")
    else:
        print("test_RecSystemOutputFiveMovies failed")

def test_RecSystemOutputZeroWhenNoID():
    id = None
    recommandedMovies = RecSystem(id)

    if recommandedMovies == 0:
        print("Es wird keine Liste zurückgegeben bei keiner ID")
    else:
        print("test_RecSystemOutputZeroWhenNoID failed")

def test_RecSystemOutputZeroWhenInvalidID():
    id = "Invalid"
    recommandedMovies = RecSystem(id)

    if recommandedMovies == 0:
        print("Es wird keine Liste zurückgegeben bei invalider ID")
    else:
        print("test_RecSystemOutputZeroWhenInvalidID failed")

test_RecSystemOutputFiveMovies()
test_RecSystemOutputZeroWhenNoID()
test_RecSystemOutputZeroWhenInvalidID()
import unittest

from app.recommendation import get_list_of_recommendation


class TestApiFunctionallity(unittest.TestCase):
    '''
    API Unit tests
    '''

    def test_RecSystemOutputFiveMovies(self) -> None:
        '''
        tests if the right length of recommended movies is given
        '''     
        id = {3}
        recommandedMovies = get_list_of_recommendation(id)

        self.assertEqual(5, len(recommandedMovies["recommendation"]))

    def test_RecSystemOutputZeroWhenNoID(self) -> None:
        '''
        tests if recommended movies empty when there is no id
        '''     
        id = {}
        recommandedMovies = get_list_of_recommendation(id)

        self.assertEqual(0, len(recommandedMovies["recommendation"]))

    def test_RecSystemOutputWithMultipleIDs(self) -> None:
        '''
        tests if recommended movies empty when there is no valid id
        '''     
        id = {8,3}
        recommandedMovies = get_list_of_recommendation(id)

        self.assertEqual(5, len(recommandedMovies["recommendation"]))


if __name__ == '__main__':
    '''
    enables execution of the tests as a seperate file for ci/cd
    '''
    unittest.main()

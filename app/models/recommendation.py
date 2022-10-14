from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Recommendation:
    '''Define the Dataclass for a Recommendation'''
    movie_id: int
    movie_title: str

    recommendations_ids: list[int]
    recommendations_titles:list[str]
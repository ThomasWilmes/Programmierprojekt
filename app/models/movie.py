from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Movie:
    '''Define the Dataclass for a Movie'''
    title: str
    m_id: int
    release_year: str
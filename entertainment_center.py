"""Project 0: Movie Trailer Website by Michael Meyerson."""

import fresh_tomatoes
import media

"""
THINGS WE WANT TO DO:
1- provide option for user to see rest of movie class details
2- use some sort of API
"""

toy_story = media.Movie('Toy Story', '1995',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

despicable_me = media.Movie('Despicable Me', '2010',
                            'https://www.youtube.com/watch?v=nVwae09eSpo')

step_brothers = media.Movie('Step Brothers', '2008',
                            'https://www.youtube.com/watch?v=_0TWeOrIYVI')

school_of_rock = media.Movie('School of Rock', '2003',
                             'https://www.youtube.com/watch?v=XCwy6lW5Ixc')

saving_private_ryan = media.Movie('Saving Private Ryan', '1998',
                                  'https://www.youtube.com/watch?v=RYExstiQlLc')  # NOQA

gladiator = media.Movie('Gladiator', '2000',
                        'https://www.youtube.com/watch?v=AxQajgTyLcM')

movies = [toy_story, despicable_me, step_brothers, school_of_rock,
          saving_private_ryan, gladiator]

fresh_tomatoes.open_movies_page(movies)

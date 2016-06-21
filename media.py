"""This module contains the definition for the Movie class."""

import json
import urllib
import webbrowser


class Movie(object):
    """This class provides a way to store movie related information.

    Attributes:
        title (str): The title of the movie.
        plot (str): A snippet explaining the plot of the movie.
        poster (str): A url for the movie's boxart.
        year (str): The year the movie was released.
        rated (str): The rating of the movie.
        released (str): The date the movie was released. Example: "09 Jul 2010"
        runtime (str): The duration of the movie.
        genre (str): A comma-separated list of categories the movie fits.
        director (str): A comma-separated list of the directors.
        writer (str): A comma-separated list of the writers.
        actors (str): A comma-separated list of the prominent actors.
        language (str): The original language of the movie.
        awards (str): A list of the awards the movie won or was nominated for.
        trailer_youtube_url (str): A url for the movie's Youtube trailer.
    """

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movie_title, movie_year, trailer_youtube):
        """Constructor function for the Movie class.

        Uses movie_title and movie_year to call OMDB API in order to retrieve
        more details about the movie. All properties from JSON response are
        set on the Movie object. See http://www.omdbapi.com/ for examples.
        """

        # Call OMDB API by supplying title & year as query params
        query_dict = {'t': movie_title, 'y': movie_year}
        api_url = 'http://www.omdbapi.com/?' + urllib.urlencode(query_dict)
        connection = urllib.urlopen(api_url)
        api_data = json.loads(connection.read())

        del api_data['Response']  # Unnecessary JSON property

        # Set API response properties on this Movie instance
        for key in api_data:
            self[key.lower()] = api_data[key]

        self.trailer_youtube_url = trailer_youtube

    def __getitem__(self, key):
        """Get property from Movie object."""
        getattr(self, key)

    def __setitem__(self, key, value):
        """Set property on Movie object."""
        setattr(self, key, value)

    def show_trailer(self):
        """Function that opens the movie's Youtube trailer in a web browser."""
        webbrowser.open(self.trailer_youtube_url)

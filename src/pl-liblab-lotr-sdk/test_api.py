import os
import unittest

from requests.models import HTTPError
from dotenv import load_dotenv

from .api import Client

# Load the API key
load_dotenv()

ROTC_ID = "5cd95395de30eff6ebccde5d"
ROTC = 'The Return of the King'


class TestMovieAPI(unittest.TestCase):
    def setUp(self):
        self.client = Client(os.getenv('THE_ONE_API_KEY'))

    def test_fetch_list_of_movies(self):
        # TODO: Replace api call with Mock
        movies = self.client.get_movie()
        return_of_the_king_id = None
        for movie in movies:
            if movie.name == ROTC:
                return_of_the_king_id = movie._id
        if return_of_the_king_id:
            self.assertEqual(return_of_the_king_id,
                             '5cd95395de30eff6ebccde5d')
        else:
            self.fail("Return of the king id not found in payload")

    def test_fetch_single_movie(self):
        # TODO: Replace api call with Mock
        movie = self.client.get_movie(movie_id=ROTC_ID)
        self.assertEqual(movie[0].name, ROTC)

    def test_fetch_list_of_quotes_from_movie(self):
        # TODO: Replace api call with Mock
        movie = self.client.get_movie(movie_id=ROTC_ID)[0]
        quotes = movie.quotes()

        for quote in quotes:
            if quote.id == "5cd96e05de30eff6ebcce7e9":
                return

        self.fail()

    def test_bad_path(self):
        # TODO: Replace api call with Mock
        def send():
            junk_path = "/foobarbaz"
            self.client._send_request(junk_path)

        self.assertRaises(HTTPError, send)

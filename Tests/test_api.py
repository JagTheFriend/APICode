# NECESSARY IMPORTS
import logging as log
import unittest

# All the files to be tested
from API import compiler_api
from API import reddit_api
from API import lyrics_api
from API import ascii_api
from API import duration_of_a_playlist_api
from API import temperature_api
from API import inspire_api

log.basicConfig(
    format="%(name)s:%(levelname)s: %(message)s",
    level=log.INFO
)


class APITests(unittest.TestCase):
    """
    These are the tests which are carried on the API    
    """
    log.info("Inside the class")

    def test_compiler(self):
        """
        Tests whether the Compiler gives:
            + the same expected output

        and makes sure the output doesn't vary
        """

        log.info("Testing the `compiler` API")
        ...

    def test_reddit(self):
        """
        Tests whether the Reddit (API) gives:
            + the expected number of posts
            + the posts from the expected Subreddit
        """

        log.info("Testing the `reddit` API")
        ...

    def test_lyrics(self):
        """
        Tests whether the `Lyrics` (API) gives:
            + the same lyrics of a song every time it is ran

        and checks whether the lyrics is accurate or not
        """

        log.info("Testing the `lyrics` API")
        ...

    def test_ascii(self):
        """
        Tests whether the `Ascii` (API) gives:
            + the same result when ran

        and checks whether the output is accurate or not
        """

        log.info("Testing the `ascii` API")
        ...

    def test_duration_of_a_playlist(self):
        """
        Tests whether the `Playlist length finder` gives:
            + the same result when ran

        and makes sure the result doesn't vary a lot
        """

        log.info("Testing the `Length finder` API")
        ...

    def test_temperature(self):
        """
        Tests whether the `Temperature` gives:
            + the same result when ran

        and checks whether the output is accurate or not
        """

        log.info("Testing the `temperature` API")
        ...

    def test_inspire(self):
        """
        Tests whether the `Inspire` (API) gives:
            + the result in the correct format
        """

        log.info("Testing the `inspire` API")
        ...

# necessary imports
from flask import Flask

# project imports
from API import compiler_api
from API import reddit_api
from API import lyrics_api
from API import ascii_api
from API import duration_of_a_playlist_api
from API import temperature_api
from API import inspire_api

app = Flask(__name__)

MAIN_API_URL = "https://complicated-api.herokuapp.com/"


@app.route('/')
def main() -> str:
    """
    A main function  
    which handles the main `index` page

    So, the wouldn't get a 404 page if they
    try to go the main page
    """

    return "Providing service to other user(s) <br> Here is my code: <a href='https://github.com/JagTheFriend/APICode'> Click me </a>"


@app.route('/compile=<lang>_<code>')
def compile(lang, code) -> dict:
    """
    To allow users to run code

    Arguments:
        @code => Code to be compiled and ran
        @lang => The langage used for compiling the code

    :return: Python dictionary
    """

    return compiler_api._compile(lang=lang, code=code)


@app.route('/reddit=<post>+<limit>')
def reddit(post, limit) -> dict:
    """
    Gets a posts from reddit
    Arguments:
        @post => Subreddit
        @limit => Total number of posts to be returned

    :return: Python dictionary
    """

    return reddit_api.supreddit(post=post, limit=limit)


@app.route('/lyrics+<song>')
def lyrics(song) -> dict:
    """
    Gets the lyrics of a song

    Arguments:
        @lyrics => Name of the lyrics

    :return: Python dictionary
    """

    return lyrics_api.song_lyrics(song)


@app.route('/ascii_<text>')
def ascii(text: str):
    """
    Makes ascii art

    Arguments:
        @text => Text to be converted to ascii art

    :return: Python Dictionary
    """

    return ascii_api.generator(text=text)


@app.route('/temp=<place>')
def temp(place: str):
    """
    It finds out the temperature of a city

    Arguments:
        @city => Name of the city

    :return: Python Dictionary
    """

    return temperature_api.temp(city=place)


@app.route('/length+<pl_id>')
def length(pl_id: str):
    """
    Gets the length of playlist

    Arguments:
        @playlist_id => This a unique id given to each playlist

    :return: Python Dictionary
    """

    return duration_of_a_playlist_api.main(pl_id)


@app.route('/inspire')
def inspire():
    """
    Gets a random inspirational text

    :return: Python dictionary
    """

    return inspire_api.main()


if __name__ == '__main__':
    app.run(debug=True)

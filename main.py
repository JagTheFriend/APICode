# necessary imports
from flask import Flask

# project imports
import compiler_api
import reddit_api
import lyrics_api
import duration_of_a_playlist

app = Flask(__name__)

MAIN_API_URL = "https://apis.theunkowncoder.repl.co/"


@app.route('/')
def main() -> str:
    """
    A main function  
    which handles the main `index` page

    So, the wouldn't get a 404 page if they
    try to go the main page
    """

    return "Providing service to other user(s) <br> Here my code: <a href='https://github.com/JagTheFriend/APICode'> Click me </a>"


@app.route('/reddit|<post>|<limit>')
def supreddit(post, limit) -> dict:
    """
    Gets a posts from reddit
    Arguments:
        @post => Subreddit
        @limit => Total number of posts to be returned

    :return: Python dictionary
    """

    return reddit_api.supreddit(post=post, limit=limit)


@app.route('/compile|<lang>|<code>')
def compile(lang, code) -> dict:
    """
    To allow users to run code

    Arguments:
        @code => Code to be compiled and ran
        @lang => The langage used for compiling the code

    :return: Python dictionary
    """
    return compiler_api._compile(lang=lang, code=code)


@app.route('/lyrics|<song>')
def lyrics(song) -> dict:
    """
    Gets the lyrics of a song

    Arguments:
        @lyrics => Name of the lyrics   

    :return: Python dictionary
    """

    return lyrics_api.song_lyrics(song)


@app.route('/playlist|<pl_id>')
def length(pl_id: str):
    """
    Gets the length of playlist 

    Arguments:
        @playlist_id => This a unique id given to each playlist

    :return: Python Dictionary
    """

    return duration_of_a_playlist.main(pl_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6969, debug=True)

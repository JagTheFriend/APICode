################################################################################
# Copyright (c) 2021 JagTheFriend
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
################################################################################

# NECESSARY IMPORTS
from flask import Flask

# project imports
from API import (
    compiler_api,
    reddit_api,
    lyrics_api,
    ascii_api,
    duration_of_a_playlist_api,
    temperature_api,
    inspire_api,
    calculator_api
)

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
    :param code: Code to be compiled and ran
    :param lang: The langage used for compiling the code
    :return: Dictionary
    """
    return compiler_api._compile(lang=lang, code=code)


@app.route('/reddit=<post>+<limit>')
def reddit(post, limit) -> dict:
    """
    Gets a posts from reddit
    :param post: Subreddit
    :param limit: Total number of posts to be returned
    :return: Dictionary
    """
    return reddit_api.supreddit(post=post, limit=limit)


@app.route('/lyrics+<song>')
def lyrics(song) -> dict:
    """
    Gets the lyrics of a song
    :param lyrics: Name of the lyrics
    :return: Dictionary
    """
    return lyrics_api.song_lyrics(song)


@app.route('/ascii_<text>')
def ascii(text: str) -> dict:
    """
    Makes ascii art
    :param text: Text to be converted to ascii art
    :return: Dictionary
    """
    return ascii_api.generator(text=text)


@app.route('/temp=<place>+<unit>')
def temp(place: str, unit: str) -> dict:
    """
    It finds out the temperature of a city
    :param city: Name of the city
    :return: Dictionary
    """
    return temperature_api.temp(city=place, unit=unit)


@app.route('/length+<pl_id>')
def length(pl_id: str) -> dict:
    """
    Gets the length of playlist
    :param pl_id: This a unique id given to each playlist
    :return: Dictionary
    """
    return duration_of_a_playlist_api.main(pl_id)


@app.route('/inspire')
def inspire() -> dict:
    """
    Gets a random inspirational text
    :return: Dictionary
    """
    return inspire_api.main()


@app.route('/cal_<string:formula>')
def calculator(formula) -> dict:
    """
    Gets the result of a calculation
    :param formula: Stuff on which calculation will be carried on Example: 5+7*9
    :return: Dictionary
    """
    return calculator_api.main(equation=formula)


@app.route('/hex+<string:hex_code>')
def hex(hex_code) -> dict:
    """
    Converts Hexadecimal code to decimal(or denary)
    :param hex_code: Stuff on which calculation will be carried on Example: 5+7*9
    :return: Dictionary
    """
    return calculator_api.hex_denary(hex_code=hex_code)


@app.route('/binary=<string:number>')
def binary(number) -> dict:
    """
    Converts Hexadecimal code to decimal(or denary)
    :param hex_code: Stuff on which calculation will be carried on Example: 5+7*9
    :return: Dictionary
    """
    return calculator_api.denary_binary(binary=number)


if __name__ == '__main__':
    app.run(debug=True)

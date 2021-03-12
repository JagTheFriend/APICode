import requests

URL = "https://complicated-api.herokuapp.com/"


def compile(*, lang, code) -> dict:
    """
    Gets the result of compiling code from the `Compiler API`
    :param lang: The language which the compiler would use to compile code
    :param code: The code to be compiled
    :return: Dictionary
    """
    return requests.get(f"{URL}/compile={lang}_{code}").json()


def reddit(*, limit: float, subreddit: str) -> dict:
    """
    Gets a limited amount of posts from a specific subreddit
    :param subreddit: Name of the subreddit
    :param limit: Number of posts to be returned
    :return: Dictionary
    """
    return requests.get(f"{URL}/reddit={' '.join(subreddit)}+{limit}").json()


def lyrics(*, song: str) -> dict:
    """
    Gets the lyrics of a song from the `Lyrics API`
    :param song: Name of the song
    :return: Dictionary
    """
    return requests.get(f"{URL}/lyrics+{song}").json()


def ascii(*, text) -> dict:
    """
    Gets Pixel art from the ASCII API
    :param text: The text which should be converted to Pixel art
    :return: Dictionary
    """
    return requests.get(f"{URL}/ascii_{text}").json()


def temp(*, place) -> dict:
    """
    Gets the weather of a place
    :param place: The name of the place whose weather would be found
    :return: Dictionary
    """
    return requests.get(f"{URL}/temp={place}").json()


def length(*, playlist: str) -> dict:
    """
    Gets the length of playlist
    :param playlist: This a unique id given to each playlist
    :return: Dictionary
    """
    return requests.get(f"{URL}/length+{playlist}").json()


def inspire() -> dict:
    """
    Gets a random inspirational text
    :return: Dictionary
    """
    return requests.get(f"{URL}/inspire").json()


def calculator(*, formula: str) -> dict:
    """
    Gets the result of a calculation
    :param formula: Stuff on which calculation will be carried on Example: 5+7*9
    :return: Dictionary
    """
    return requests.get(f"{URL}/cal_{formula}").json()


def hex_to_denary(*, hex_code) -> dict:
    """
    Converts Hexadecimal code to decimal(or denary)
    :param formula: Stuff on which calculation will be carried on Example: 5+7*9
    :return: Dictionary
    """
    return requests.get(f"{URL}/hex_to_denary+{hex_code}").json()

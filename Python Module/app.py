import requests

URL = "https://complicated-api.herokuapp.com/"

def compile(*, lang, code):
    """
    Gets the result of compiling code from the `Compiler API`


    """

def ascii(*, text) -> dict:
    """
    Gets Pixel art from the API

    :param text: The text which should be converted to Pixel art
    :return: Dictionary
    """

    return requests.get(f"https://complicated-api.herokuapp.com/ascii_{text}").json()


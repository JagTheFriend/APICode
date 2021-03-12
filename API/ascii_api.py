from art import text2art
import random


def generator(*, text) -> dict:
    """
    Makes ascii art
    :param text: Text to be converted to ascii art
    :return: Dictionary
    """

    return {"output": text2art(text)}

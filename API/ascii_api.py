from art import text2art
import random


def generator(*, text: str) -> dict:
    """
    Makes ascii art
    :param text: Text to be converted to ascii art
    :return: Dictionary
    """
    return {"output": text2art(text)}

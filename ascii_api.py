from art import text2art
import random

def generator(*, text) -> dict:
    """
    Makes ascii art

    Arguments:
        @text => Text to be converted to ascii art
    
    :return: Python Dictionary
    """
    
    return {"output":text2art(text)}

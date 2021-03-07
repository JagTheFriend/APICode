from art import text2art
import random

def generator(*, text) -> dict:
    return {"output":text2art(text)}

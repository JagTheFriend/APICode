import requests


def main() -> dict:
    """
    Gets a random inspirational text

    :return: Python Dictionary
    """
    res = requests.get("https://zenquotes.io/api/random").json()[0]
    result = {}
    result["output"] = {}
    result["output"]["description"] = res["q"]
    result["output"]["author"] = res["a"]

    return result

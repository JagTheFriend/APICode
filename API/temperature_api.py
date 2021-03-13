import requests
import os

appid = os.environ.get('weather')


def temp(*, city) -> dict:
    """
    It finds out the temperature of a city
    :param city: Name of the city
    :return: Dictionary
    """

    result = {}
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}&units=metric'
    try:
        data = requests.get(url).json()
        result["output"] = {}
        result["output"]["temp"] = data['main']['temp']
        result["output"]["wind_speed"] = data['wind']['speed']

        result["output"]["latitude"] = data['coord']['lat']
        result["output"]["longitude"] = data['coord']['lon']

        result["output"]["descriptions"] = data['weather'][0]['description']

    except Exception:
        result["output"] = "Invalid City name | Or the API Does not understand"

    return result

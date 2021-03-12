import requests
import os

appid = os.environ.get('weather')


def temp(*, city) -> dict:
    """
    It finds out the temperature of a city

    Arguments:
        :param city: Name of the city

    :return: Dictionary
    """

    result = {}
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}&units=metric'
    try:
        data = requests.get(url).json()
        result["temp"] = data['main']['temp']
        result["wind_speed"] = data['wind']['speed']

        result["latitude"] = data['coord']['lat']
        result["longitude"] = data['coord']['lon']

        result["descriptions"] = data['weather'][0]['description']

    except Exception:
        result["output"] = "Invalid City name | Or the API Does not understand"

    return result

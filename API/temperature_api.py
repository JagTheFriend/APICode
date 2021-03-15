import requests
import os

appid = os.environ.get('weather')


def temp(*, city: str, unit: str = "metric") -> dict:
    """
    Gets the weather of a place
    :param place: The name of the place whose weather would be found
    :param unit: The unit used for measuring amounts, (it can be either 'metric' or 'imperial)
    :return: Dictionary
    """
    unit = "metric" if unit not in ["metric", "imperial"] else unit
    result = {}
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}&units={unit}'
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

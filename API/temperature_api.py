################################################################################
# Copyright (c) 2021 JagTheFriend
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
################################################################################

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

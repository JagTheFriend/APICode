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
import json

AI_KEY = os.environ.get("AI")

URL = "https://api.pgamerx.com/v3/ai/response?message=encodeURIComponent('{message}')&type=stable"
header = {'x-api-key': AI_KEY}

def _ai(*, message: str = "Hello gamer") -> dict:
    """
    Allow you to talk with an `AI` 
    :param message: The text the `AI` would process
    :return: Dictionary
    """
    response = requests.get(
        URL.format(message=message),
        headers=header
    ).json()[0]["message"]
    # response = json.loads(response)[0]["message"]
    return {"output": response}#URL.format(message=message)}

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


import aiml
# from prsaw import RandomStuff
# rs = RandomStuff()

# setup
aiml_kernel = aiml.Kernel()
bot_brain = "bot_brain.brn"

try:
    # aiml_kernel.bootstrap(learnFiles="API/AI_Train_Data/std-startup.xml",commands="load aiml b")
    # aiml_kernel.saveBrain("bot_brain.brn")
    aiml_kernel.bootstrap(brainFile=bot_brain)
except Exception:
    pass

def _ai(*, message: str = "Hello gamer") -> dict:
    """
    Allow you to talk with an `AI` 
    :param message: The text the `AI` would process
    :return: Dictionary
    """
    return {"output": get_response(message)}


def get_response(message: str) -> str:
    """
    This is a back up, just in case the first function fails.
    :return: String    
    """
    if not message:
        return "Ask me anything"
    # processing response
    aiml_response = aiml_kernel.respond(message)

    # we can't send an empty message, is the message empty?
    if aiml_response == '':
        return "whaaat ?"
    # sending the correct response.
    else:
        return aiml_response

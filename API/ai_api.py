import aiml
from prsaw import RandomStuff

# setup
aiml_kernel = aiml.Kernel()
bot_brain = "API\\bot_brain.brn"

aiml_kernel.bootstrap(brainFile=bot_brain)

rs = RandomStuff()


def _ai(*, message: str = "Hello gamer") -> dict:
    """
    Allow you to talk with an `AI` 
    :param message: The text the `AI` would process
    :return: Dictionary
    """
    try:
        return {"output": rs.get_ai_response(message)}
    except Exception:  # some error did occur
        return {"output": backup(message)}


def backup(message: str) -> str:
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

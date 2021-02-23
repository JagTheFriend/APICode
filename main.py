# necessary imports
from flask import Flask

# project imports
import compiler_api
import meme_api


app = Flask(__name__)

@app.route('/reddit=<post>+<limit>')
def supreddit(post, limit):
    """Gets a posts from reddit
    Arguments:
    @post => Subreddit
    @limit => Total number of posts to be returned

    :return: Python dictionary"""

    return meme_api.supreddit(post=post, limit=limit)


@app.route('/compile=<lang>+<code>')
def compile(lang, code):
    """To allow users to run code
    Arguments:
    @code => Code to be compiled and ran
    @lang => The langage used for compiling the code

    :return: Python dictionary"""

    return compiler_api._compile(lang=lang, code=code)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6969, debug=False)

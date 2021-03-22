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

import praw
import os

# The bot is logging in
reddit = praw.Reddit(
    client_id=os.environ.get("reddit_id"),
    client_secret=os.environ.get("reddit_secret"),
    user_agent="python",
    username=os.environ.get("reddit_name"),
    password=os.environ.get("reddit_password")
)


def supreddit(*, post: str, limit: int) -> dict:
    """
    Gets a certain number of posts from a subreddit
    :param post: Name of the subreddit
    :param limit: Number of results to be returned
    :return: Dictionary
    """
    if str(limit).isdigit():
        limit = int(limit)
    else:
        return {"Error": "Please give a number for the number of posts to be returned"}

    # to store the results
    result = {}
    try:
        subreddit = reddit.subreddit(post)
    except Exception:
        result["output"] = "No a valid subreddit"
        return result

    tops = subreddit.top(limit=limit)

    for i in tops:
        result[str(i.title)] = {}
        result[str(i.title)]["NSFW"] = bool(i.over_18)
        result[str(i.title)]["Title"] = str(i.title)

        result[str(i.title)]["Description"] = str(i.selftext) if bool(
            i.selftext) else "No Description Provided"
        result[str(i.title)]["Number_Of_Comments"] = str(i.num_comments)

        result[str(i.title)]["Post_URL"] = str(
            reddit.config.reddit_url+i.permalink)
        result[str(i.title)]["Image_URL"] = str(i.url)

    return result

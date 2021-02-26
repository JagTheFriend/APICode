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


def supreddit(*, post, limit):
    """Gets memes from reddit

    :param post: Name of the subreddit
    :param limit: Number of results to be returned

    :return: Python dictionary"""

    if str(limit).isdigit():
        limit = int(limit)
    else:
        return {"Error": "Please give a number got the limit of subreddits to be returned"}

    subreddit = reddit.subreddit(post)
    tops = subreddit.top(limit=limit)

    # to store the results
    result = {}

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

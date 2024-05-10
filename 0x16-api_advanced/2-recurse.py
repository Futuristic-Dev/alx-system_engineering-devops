#!/usr/bin/python3

"""
Write a recursive function that queries the Reddit API.

Returns a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should.
Return None.
Hint: The Reddit API uses pagination for separating pages of responses.
"""


from requests import get
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    Query the Reddit API recursively.

    Returns a list containing the titles of all hot articles.
    For a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'api_advanced-project'
    }
    params = {'after': after}
    results = requests.get(url, params=params, headers=headers)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is None:
            return hot_list
        else:
            after = after_data
            for post in results.json().get("data").get("children"):
                hot_list.append(post.get("data").get("title"))
            return recurse(subreddit, hot_list, after)
    else:
        return None

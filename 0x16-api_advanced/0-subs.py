#!/usr/bin/python3

"""
Write a function that queries the reddit API.

Returns the number of subscribers (not active users, total subscribers).
For a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""


from requests import get


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and returns the number of subscribers.

    for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'Google Chrome Version 81.0.4044.129'
    }
    response = get(url, headers=headers, allow_redirects=False)
    result = response.json()

    if response.status_code != 200:
        return 0

    try:
        return result.get('data').get('subscribers')

    except Exception:
        return 0

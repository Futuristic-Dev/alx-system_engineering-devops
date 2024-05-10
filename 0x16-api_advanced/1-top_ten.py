#!/usr/bin/python3

"""
Write a function that queries the Reddit API.

Print the titles of the first 10 hot posts listed for\n
a given subreddit.
"""


from requests import get


def top_ten(subreddit):
    """
    Query the Reddit API.

    Print the titles of the first 10 hot posts listed\n
    for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {
        'User-Agent': 'Google Chrome Version 81.0.4044.129'
    }

    response = get(url, headers=headers, allow_redirects=False)
    result = response.json()

    if response.status_code != 200:
        print(None)
        return

    try:
        for post in result.get('data').get('children'):
            print(post.get('data').get('title'))

    except Exception:
        print("None")

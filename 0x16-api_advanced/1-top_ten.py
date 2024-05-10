#!/usr/bin/python3

"""
Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
"""

from requests import get

def top_ten(subreddit):
    

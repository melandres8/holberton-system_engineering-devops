#!/usr/bin/python3
"""
    How many subs
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers

    Args:
        subreddit (string): Particular topic
    """
    url = 'https://api.reddit.com/r/{}/about'.format(subreddit)
    headers = {'User-Agent': 'Alien'}
    response = requests.get(url, headers=headers).json()
    try:
        return response.get('data').get('subscribers')
    except Exception:
        return 0

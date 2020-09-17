#!/usr/bin/python3
"""
    How many subs
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10
    hot posts listed for a given subreddit.

    Args:
        subreddit (string): Particular topic
    """
    url = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
    headers = {'User-Agent': 'Alien'}
    payload = {'h': 'all', 'limit': 10}
    response = requests.get(url, headers=headers, params=payload).json()
    try:
        posts = response.get('data').get('children')
        for hot in posts:
            print(hot.get('data').get('title'))
    except Exception:
        print('None')

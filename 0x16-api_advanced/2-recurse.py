#!/usr/bin/python3
"""
    Recurse it!
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """ eturns a list containing the titles
        of all hot articles for a given subreddit.
        If no results are found for the given
        subreddit, the function should return None.

    Args:
        subreddit (string): Particular topic
        hot_list (list, strings): ist containing the titles
        of all hot articles. Defaults to [].
    """
    url = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
    headers = {'User-Agent': 'Alien'}
    payload = {'h': 'all', 'after': after}
    response = requests.get(url, headers=headers, params=payload).json()
    try:
        posts = response.get('data').get('children')
        _next = response.get('data').get('after')
        for post in posts:
            hot_list.append(post.get('data').get('title'))
        if _next is not None:
            recurse(subreddit, hot_list, _next)
        return hot_list
    except Exception:
        return None

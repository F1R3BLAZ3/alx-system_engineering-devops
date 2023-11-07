#!/usr/bin/python3
"""
Queries the Reddit API recursively and returns a list
of hot article titles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetches hot article titles from the Reddit API.

    Args:
        subreddit (str): The subreddit to search for hot articles.
        hot_list (list): A list to store hot article titles.
        after (str): The "after" parameter used for pagination.

    Returns:
        list: A list containing hot article titles.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            children = data['data']['children']
            for child in children:
                hot_list.append(child['data']['title'])

            after = data['data']['after']
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        except (KeyError, ValueError):
            # Invalid data or format
            return None
    else:
        # Invalid subreddit or other error
        return None

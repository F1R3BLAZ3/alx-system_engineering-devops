#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing
the titles of all hot articles
for a given subreddit. Uses a recursive approach for pagination.

Requirements:
- Uses the Requests module for sending HTTP requests to the Reddit API
- Follows the PEP 8 style
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetches the titles of all hot articles for a subreddit.

    :param subreddit: The name of the subreddit.
    :param hot_list: A list to store the titles (default is an empty list).
    :param after: The 'after' parameter for pagination (default is None).
    :return: A list of article titles or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    if after:
        url += f"?after={after}"

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                print(title)

            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
        except (KeyError, ValueError):
            # Invalid data or format
            return None
    else:
        # Invalid subreddit or other error
        return None

    return hot_list

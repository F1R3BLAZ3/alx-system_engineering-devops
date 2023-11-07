#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit.
If the subreddit is invalid or there is an issue with the request,
it prints None.

Requirements:
- Uses the Requests module for sending HTTP requests to the Reddit API
- Follows the PEP 8 style
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a subreddit.

    :param subreddit: The name of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

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
        except (KeyError, ValueError):
            # Invalid data or format
            print("None")
    else:
        # Invalid subreddit or other error
        print("None")

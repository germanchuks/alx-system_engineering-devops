#!/usr/bin/python3
"""Script that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given
    subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "My-User-Agent"}
    params = {
        "limit": 10
    }

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code >= 300:
        print("None")
    else:
        [print(child.get("data").get("title"))
         for child in response.json().get("data").get("children")]

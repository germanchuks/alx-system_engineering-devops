#!/usr/bin/python3
"""Script that queries the Reddit API and returns the number of subscribers
for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My-User-Agent"}

    response = requests.get(url,
                            headers=headers,
                            allow_redirects=False)
    if response.status_code >= 300:
        return 0
    else:
        data = response.json().get("data")
        subscribers = data.get("subscribers")
        return subscribers

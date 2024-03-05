#!/usr/bin/python3
"""Script that queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit."""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Recursively retrieves a list of titles of all hot posts on a given
    subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): List to store post titles.
                                    Default is an empty list.
        after (str, optional): Token used for pagination.
                                Default is an empty string.
        count (int, optional): Current count of retrieved posts. Default is 0.

    Returns:
        list: A list containing titles of all hot articles of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "My-User-Agent"}
    params = {
        "count": count,
        "after": after,
    }

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    info = response.json()
    hot_list += [child.get("data").get("title")
                 for child in info.get("data").get("children")]

    if not info.get("data").get("after"):
        return hot_list

    return recurse(subreddit, hot_list, info.get("data").get("after"),
                   info.get("data").get("dist"))

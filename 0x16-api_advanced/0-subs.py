#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests # type: ignore


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Sandra/2.5"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data.get['data', {}].get['subscribers', 0]
        return subscribers
    else:
        return 0

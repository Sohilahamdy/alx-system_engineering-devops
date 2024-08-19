#!/usr/bin/python3
"""
Contains the recurse function
"""

import requests


def recurse(subreddit, hot_list=[]):
    """Returns a list of all hot articles for a given subreddit"""
    if not isinstance(subreddit, str) or not subreddit:
        return None

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        'User-Agent': (
             '0x16-api_advanced:project:v1.0.0 (by /u/your_username)'
        )
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json().get('data', {})
            posts = data.get('children', [])
            if posts:
                for post in posts:
                    hot_list.append(post.get('data', {}).get('title', ''))

                # Get the next page
                after = data.get('after', None)
                if after:
                    next_url = (
                        f'https://www.reddit.com/r/{subreddit}/hot.json'
                        f'?after={after}'
                    )

                    # Recursive call with updated hot_list
                    return recurse(subreddit, hot_list)
                else:
                    return hot_list
            else:
                return None
        except ValueError:
            return None
    else:
        return None

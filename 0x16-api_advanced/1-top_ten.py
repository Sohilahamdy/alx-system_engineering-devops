#!/usr/bin/python3
"""
Contains the top_ten function
"""

import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit"""
    if not isinstance(subreddit, str) or not subreddit:
        print("None")
        return

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/your_username)'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        try:
            data = response.json().get('data', {})
            posts = data.get('children', [])
            if posts:
                for post in posts[:10]:
                    print(post.get('data', {}).get('title', ''))
            else:
                print("None")
        except ValueError:
            print("None")
    else:
        print("None")

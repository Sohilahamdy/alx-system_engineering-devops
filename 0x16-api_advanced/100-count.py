#!/usr/bin/python3
"""
Contains the count_words function
"""

import requests
import re
from collections import defaultdict

def count_words(subreddit, word_list):
    """Counts occurrences of words in titles of hot articles in a subreddit"""
    
    def get_hot_posts(subreddit, after=None):
        """Fetch hot posts recursively"""
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
        headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/your_username)'}
        params = {'after': after} if after else {}
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code == 200:
            try:
                data = response.json().get('data', {})
                posts = data.get('children', [])
                after = data.get('after', None)
                return posts, after
            except ValueError:
                return [], None
        else:
            return [], None
    
    def count_words_recursive(subreddit, word_list, hot_list=[], after=None):
        """Recursive function to get all posts and count keywords"""
        posts, new_after = get_hot_posts(subreddit, after)
        
        if posts:
            for post in posts:
                title = post.get('data', {}).get('title', '').lower()
                hot_list.extend(title)
            
            if new_after:
                return count_words_recursive(subreddit, word_list, hot_list, new_after)
            else:
                return hot_list
        else:
            return hot_list

    # Validate subreddit and word_list
    if not isinstance(subreddit, str) or not isinstance(word_list, list):
        return
    
    if not word_list:
        return
    
    word_list = [word.lower() for word in word_list]
    hot_list = count_words_recursive(subreddit, word_list)
    
    # Create a dictionary to store word counts
    word_count = defaultdict(int)
    
    # Define a regex pattern for matching words only
    word_pattern = re.compile(r'\b\w+\b')

    for title in hot_list:
        for word in word_list:
            word_count[word] += len(word_pattern.findall(title))
    
    # Sort words first by count (descending) then alphabetically
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    
    for word, count in sorted_words:
        if count > 0:
            print(f"{word}: {count}")

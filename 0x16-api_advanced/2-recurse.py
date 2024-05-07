#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.
"""
import requests

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    """Set a custom User-Agent header"""
    headers = {'User-Agent': 'MyRedditBot/1.0'} 
    params = {'after': after} if after else None

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])

            after = data['data']['after']
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        elif response.status_code >= 400:
            """Invalid subreddit"""
            return None
        else:
            """If Other error occurred"""
            return None
    except requests.RequestException:
        """If Request exception occurred"""
        return None
#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    """Set a custom User-Agent header"""
    headers = {'User-Agent': 'MyRedditBot/1.0'}  

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for i in range(min(10, len(posts))):
                title = posts[i]['data']['title']
                print(f"{i+1}. {title}")
        elif response.status_code >= 400:
            """Invalid subreddit"""
            print(None)
        else:
            """If Other error occurred"""
            print(None)
    except requests.RequestException:
        """If Request exception occurred"""
        print(None)
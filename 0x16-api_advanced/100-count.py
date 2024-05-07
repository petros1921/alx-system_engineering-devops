#!/usr/bin/python3
"""
recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not).
"""
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

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
                title = post['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title.split():
                        counts[word] = counts.get(word, 0) + 1

            after = data['data']['after']
            if after is not None:
                return count_words(subreddit, word_list, after, counts)
            else:
                sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
                for keyword, count in sorted_counts:
                    print(f"{keyword}: {count}")
        elif response.status_code == 404:
            """Invalid subreddit"""
            return None
        else:
            """If Other error occurred"""
            return None
    except requests.RequestException:
        """If Request exception occurred"""
        return None
#!/usr/bin/python3
"""A function that queries the Reddit API and 
prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    print title of first 10 hot posts.

    :param subreddit: The name of the subreddit.
    :return: None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyBot/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
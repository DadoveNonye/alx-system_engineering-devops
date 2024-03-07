#!/usr/bin/python3
"""A function that queries the Reddit API """

import requests


def number_of_subscribers(subreddit):
   """
    Get the number of subscribers for a given subreddit.

    :param subreddit: The name of the subreddit.
    :return: 0
    """
   url = f"https://www.reddit.com/r/{subreddit}/about.json"
   headers = {"User-Agent": "Mozilla/5.0"}
   response = requests.get(url, headers=headers,  allow_redirects=False)

   if response.status_code == 200:
      data = response.json()
      subscribers = data['data']['subscribers']
      return subscribers
   else:
      return 0
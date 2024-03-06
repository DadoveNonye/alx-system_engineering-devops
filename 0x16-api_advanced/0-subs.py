#!/usr/bin/python3
#  A function that queries the Reddit API 
import requests
def number_of_subscribers(subreddit):
   url = f"https://www.reddit.com/r/{subreddit}/about.json"
   headers = {'User-Agent': 'Dadove/1.0'}
   response = requests.get(url, headers=headers)

   if response.status_code == 200:
      data = response.json()
      subscribers = data['data']['subscribers']
      return subscribers
   else:
      return 0
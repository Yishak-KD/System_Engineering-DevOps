#!/usr/bin/python3
# A script that returns 10 titles

import requests

def top_ten(subreddit):
    """Function that returns 10 titles in a subreddit"""

    url = "https://www.reddit.com/r/" + subreddit + "/hot/json"

    headers = {'User-Agent': 'ALX'}
    params = {
            "limit": 10
    }
    r = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if r.status_code == 200:
        for i in r.json().get("data").get("children"):
            print(i.get("data").get("title"))
    else:
        print("None")

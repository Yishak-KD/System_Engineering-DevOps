#!/usr/bin/python3
# A script that returns number of subcribers

import requests

def number_of_subscribers(subreddit):
    """Function that returns number of subcribers from an API"""

    url = "https://www.reddit.com/r/" + subreddit + "/about.json"

    headers = {'User-Agent': 'ALX'}

    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        return r.json().get("data", None).get("subscribers", None)
    else:
        return 0

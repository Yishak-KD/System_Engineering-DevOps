#!/usr/bin/python3
# A script that returns number of subcribers

import requests


def number_of_subscribers(subreddit):
    """
    Function that returns number of subcribers from an API
    """

    url = "https://www.reddit.com/r/" + subreddit + "/about.json"

    headers = {
        'User-Agent': 'ALX',
        'From': 'alxstud.tech'
    }

    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        res = r.json().get('data')
        return res.get("subscribers")
    else:
        return 0
if __name__ == "__main__":
    pass

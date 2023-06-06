#!/usr/bin/python3
"""
Python script that sends a search request to the Twitter API
"""
import requests
import base64
import sys


if __name__ == "__main__":
    client_key = sys.argv[1]
    client_secret = sys.argv[2]

    key_s = '{}:{}'.format(client_key, client_secret).encode('ascii')
    b64_key = base64.b64encode(key_s)
    b64_key = b64_key.decode('ascii')

    b_url = 'https://api.twitter.com/'
    a_url = '{}oauth2/token'.format(b_url)

    a_headers = {
        'Authorization': 'Basic {}'.format(b64_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }

    a_data = {
        'grant_type': 'client_credentials'
    }

    a_resp = requests.post(a_url, headers=a_headers, data=a_data)

    access_token = a_resp.json().get('access_token')

    s_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    s_params = {
        'q': sys.argv[3],
        'result_type': 'recent',
        'count': 5
    }

    s_url = '{}1.1/search/tweets.json'.format(b_url)
    s_resp = requests.get(s_url, headers=s_headers, params=s_params)

    tweet_data = s_resp.json()

    for x in tweet_data['statuses']:
        print("[{}] {} by {}".format(x.get('id'), x.get('text'),
                                     x.get('user').get('name')))

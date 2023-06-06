#!/usr/bin/python3
"""
Python script that sends a search request to the
Star Wars API, searching people
"""
import requests
import sys


if __name__ == "__main__":
    page = 1

    films = {}

    for num in range(1, 8):
        url = 'https://swapi.co/api/films/{}/'.format(num)
        r = requests.get(url)
        films[url] = r.json().get('title')

    while page:
        s = sys.argv[1]
        url = 'https://swapi.co/api/people/?search={}&page={}'.format(s, page)
        r = requests.get(url)
        json_o = r.json()
        if page == 1:
            print("Number of results: {}".format(json_o.get('count')))
        for character in json_o.get('results'):
            print(character.get('name'))
            for film in character.get('films'):
                print("\t{}".format(films[film]))
        if not json_o.get('next'):
            break
        page += 1

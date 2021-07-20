#! /usr/bin/env python3
# coding utf-8

import requests


class ApiWikiMedia:
    def __init__(self, city) -> None:
        self.city = city
        self.url = f"https://fr.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles={self.city}"
        self.content = requests.get(self.url)
        self.history = self.get_content()

    def get_content(self):
        history = self.content.json()
        pageid = str(history["query"]["pages"])
        pageid = pageid.split("{")[1][1:-3]
        history = str(history["query"]["pages"][pageid]["extract"])
        history = str(history.split(".")[0:4])[2:-2]
        return history


if __name__ == "__main__":
    rennes = ApiWikiMedia("Paris")
    print(rennes.content)
    print(rennes.history)

#! /usr/bin/env python3
# coding utf-8

import random

import requests

class ApiWikiMedia:
    def __init__(self, city) -> None:
        self.city = city
        self.content = self.get_content()
    
    def get_content(self):
        url = f"https://fr.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles={self.city}"
        content = requests.get(url).json()
        pageid = str(content["query"]["pages"]).split("{")[1][1:-3]
        content = str(content["query"]["pages"][pageid]["extract"])
        content = str(content.split(".")[0:2])[2:-2]
        return content
    
if __name__ == "__main__":
    rennes = ApiWikiMedia("Paris")
    print(rennes.content)
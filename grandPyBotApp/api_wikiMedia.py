#! /usr/bin/env python3
# coding utf-8

import requests


class ApiWikiMedia:
    def __init__(self, keyWord) -> None:
        """This class retrieves data from the wikipedia API

        Args:
            keyWord (str): the keyword is the incoming data for the wikipedia API 
        """
        self.keyWord = keyWord
        self.url = f"https://fr.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles={self.keyWord}"
        self.history = self.get_content()
    
    def get_content(self):
        if self.keyWord != "":
            content = requests.get(self.url)
            if content.status_code == 200:
                history = content.json()
                pageid = str(history["query"]["pages"])
                print(pageid)
                pageid = pageid.split("{")[1][1:-3]
                if int(pageid) != -1:
                    history = str(history["query"]["pages"][pageid]["extract"])
                    history = str(history.split(".")[0:3])[2:-2]
                    return f"Tu savais que ... {history}"
                else:
                    return f"Je ne connais pas {self.keyWord} mon poussin, tu peux m'en dire plus"
        else:
            return "Je dois être fatigué, tu peux reformuler mon petit?"


if __name__ == "__main__":
    rennes = ApiWikiMedia("openclassrooms")
    print(rennes.history)

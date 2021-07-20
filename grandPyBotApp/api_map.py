#! /usr/bin/env python3
# coding utf-8

import requests

apiKeyMap = "AIzaSyCXkeG_ML2KTexqdiATu3n3j1DLIM2_njA"


class ApiMap:
    def __init__(self, keyWord: str) -> str:
        """[summary]

        Args:
            keyWord (str): [description]

        Returns:
            str: [description]
        """
        self.keyWord = keyWord
        self.urlMap = f"https://maps.googleapis.com/maps/api/geocode/json?address={self.keyWord}&key={apiKeyMap}"
        self.adress = self.get_adress()
        self.adressMap = self.get_adress_map()
        self.imgMap = self.get_imgMap()

    def get_adress(self):
        response = requests.get(self.urlMap)
        if response.status_code == 200:
            content = response.json()
            if content['results'] != []:
                return content["results"][0]['formatted_address']
        else:
            return f"{self.keyWord} ? Je n'ai pas compris ce que tu m'as dis"

    def get_adress_map(self):
        adressMap = str(self.adress)
        adressMap = adressMap.replace(" ", "+")
        return adressMap

    def get_imgMap(self):
        if self.adressMap:
            return f"""https://maps.googleapis.com/maps/api/staticmap?center={self.adressMap}&zoom=13&size=600x300&maptype=roadmap&markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318&markers=color:red%7Clabel:C%7C40.718217,-73.998284&key={apiKeyMap}"""
        else:
            return "grandPyBotApp/static/papy.png"

if __name__ == "__main__":
    apiMap1 = ApiMap("vivement les vacances")
    print(apiMap1.keyWord)
    print(apiMap1.adress)
    print(apiMap1.adressMap)
    print(apiMap1.urlMap)

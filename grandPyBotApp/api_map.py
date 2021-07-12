#! /usr/bin/env python3
# coding utf-8

import requests

apiKeyMap = "AIzaSyCXkeG_ML2KTexqdiATu3n3j1DLIM2_njA"

class ApiMap:
    def __init__(self, keyWord:str) -> str:
        """[summary]

        Args:
            keyWord (str): [description]

        Returns:
            str: [description]
        """
        self.keyWord = keyWord
        self.urlMap = f"https://maps.googleapis.com/maps/api/geocode/json?address={keyWord}&key={apiKeyMap}"
        self.content = requests.get(self.urlMap).json()
        self.adress = self.get_adress()
        self.gps = self.get_gps()
        self.city = self.get_city()
        self.adressMap = self.get_adress_map()
        self.imgMap = f"""https://maps.googleapis.com/maps/api/staticmap?center={self.adressMap}&zoom=13&size=600x300&maptype=roadmap&markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318&markers=color:red%7Clabel:C%7C40.718217,-73.998284&key={apiKeyMap}"""
    
    def get_adress(self):
        adress = self.content['results'][0]['formatted_address']
        return adress
    
    def get_adress_map(self):
        adressMap = str(self.adress)
        adressMap = adressMap.replace(" ", "+")
        return adressMap
    
    def get_gps(self):
        lat = self.content['results'][0]['geometry']['location']['lat']
        lng = self.content['results'][0]['geometry']['location']['lng']
        return f"{lat}, {lng}"
    
    def get_city(self):
        return self.content['results'][0]['address_components'][2]['long_name']

if __name__== "__main__":
    apiMap1 = ApiMap("Openclassrooms")
    print(apiMap1.keyWord)
    print(apiMap1.adress)
    print(apiMap1.adressMap)
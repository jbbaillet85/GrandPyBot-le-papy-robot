#! /usr/bin/env python3
# coding utf-8

from grandPyBotApp.api_map import ApiMap
from config import apiKeyMap

apiMap = ApiMap("Openclassrooms")

def test_api_keyWord():
    assert apiMap.keyWord == "Openclassrooms"

def test_api_urlmap():
    assert apiMap.urlMap == f"https://maps.googleapis.com/maps/api/geocode/json?address={apiMap.keyWordkeyWord}&key={apiKeyMap}"

def test_api_map_adress():
    assert apiMap.adress == "10 Quai de la Charente, 75019 Paris"

def test_api_map_gps():
    assert apiMap.gps == "48.8974838301304, 2.3835133039538903"
#! /usr/bin/env python3
# coding utf-8

import requests

from grandPyBotApp.api_map import ApiMap, apiKeyMap

apiMap = ApiMap("Openclassrooms")


def test_ApiMap(monkeypatch):
    results = {'results': [
        {'address_components': [
            {'long_name': '10', 'short_name': '10', 'types': ['street_number']}, 
            {'long_name': 'Quai de la Charente', 'short_name': 'Quai de la Charente', 'types': ['route']}, 
            {'long_name': 'Paris', 'short_name': 'Paris', 'types': ['locality', 'political']}, 
            {'long_name': 'Département de Paris', 'short_name': 'Département de Paris', 'types': ['administrative_area_level_2', 'political']}, 
            {'long_name': 'Île-de-France', 'short_name': 'IDF', 'types': ['administrative_area_level_1', 'political']}, 
            {'long_name': 'France', 'short_name': 'FR', 'types': ['country',                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        'political']}, {'long_name': '75019', 'short_name': '75019', 'types': ['postal_code']}], 
         'formatted_address': '10 Quai de la Charente, 75019 Paris, France', 
         'geometry': {'location': {'lat': 48.8975156, 'lng': 2.3833993}, 
                      'location_type': 'ROOFTOP', 'viewport': 
                          {'northeast': {'lat': 48.8988645802915, 'lng': 2.384748280291502}, 
                           'southwest': {'lat': 48.8961666197085, 'lng': 2.382050319708498}}}, 
         'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8', 'plus_code': {'compound_code': 'V9XM+29 Paris, France', 'global_code': '8FW4V9XM+29'}, 'types': ['establishment', 'point_of_interest']}], 'status': 'OK'}

    def mockApiMap():
        return results

    monkeypatch.setattr(requests, 'get', mockApiMap)
 
    assert apiMap.adress == '10 Quai de la Charente, 75019 Paris, France'
    assert apiMap.adressMap == "10+Quai+de+la+Charente,+75019+Paris,+France"
    assert apiMap.gps == "48.8975156, 2.3833993"
    assert apiMap.city == "Paris"


def test_api_keyWord():
    assert apiMap.keyWord == "Openclassrooms"


def test_api_urlmap():
    assert apiMap.urlMap == f"https://maps.googleapis.com/maps/api/geocode/json?address={apiMap.keyWord}&key={apiKeyMap}"

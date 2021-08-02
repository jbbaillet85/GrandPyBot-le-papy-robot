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

    assert apiMap.adress == '10 Quai de la Charente, 75019 Paris, France' or "Je n'ai pas compris ce que tu m'as dis mon poussin"
    assert apiMap.adressMap == apiMap.adress.replace(' ', "+")


def test_api_keyWord():
    assert apiMap.keyWord == "Openclassrooms"


def test_api_urlmap():
    assert apiMap.urlMap == f"https://maps.googleapis.com/maps/api/geocode/json?address={apiMap.keyWord}&key={apiKeyMap}"

def test_imgMap():
    assert apiMap.imgMap == f"""https://maps.googleapis.com/maps/api/staticmap?center={apiMap.adressMap}&zoom=13&size=600x300&maptype=roadmap&
    markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318&markers=color:red%7Clabel:C%7C40.718217,-73.998284&
    key={apiKeyMap}""" or 'static/papy.png'

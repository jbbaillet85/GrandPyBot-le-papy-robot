#! /usr/bin/env python3
# coding utf-8

import requests

from grandPyBotApp.api_wikiMedia import ApiWikiMedia

openclassrooms = ApiWikiMedia("Paris")


def test_ApiWikipedia(monkeypatch):
    results = "<Response [200]>"
    
    def mockApiWikipedia(requests):
        return results

    monkeypatch.setattr(requests, 'get', mockApiWikipedia)
    assert openclassrooms.city == "Paris"
    assert openclassrooms.url == "https://fr.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=Paris"
    assert openclassrooms.history == "Paris (/pa', 'ʁi/) est la commune la plus peuplée et la capitale de la France"
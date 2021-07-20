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
    assert openclassrooms.keyWord == "Paris"
    assert openclassrooms.url == "https://fr.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=Paris"
    assert openclassrooms.history == """Tu savais que ... Paris (/pa', 'ʁi/) est la commune la plus peuplée et la capitale de la France', "\nElle se situe au cœur d'un vaste bassin sédimentaire aux sols fertiles et au climat tempéré, le bassin parisien, sur une boucle de la Seine, entre les confluents de celle-ci avec la Marne et l'Oise"""

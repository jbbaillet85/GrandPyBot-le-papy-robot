#! /usr/bin/env python3
# coding utf-8

import requests

from grandPyBotApp.api_wikiMedia import ApiWikiMedia

rennes = ApiWikiMedia("Paris")


def test_ApiWikipedia(monkeypatch):
    results = "Paris (/pa', 'ʁi/) est la commune la plus peuplée et la capitale de la France"
    def mockApiWikipedia():
        return results

    monkeypatch.setattr(requests, 'get', mockApiWikipedia)
 
    assert rennes.content == "Paris (/pa', 'ʁi/) est la commune la plus peuplée et la capitale de la France"
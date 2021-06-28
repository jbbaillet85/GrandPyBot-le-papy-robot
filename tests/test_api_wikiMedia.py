#! /usr/bin/env python3
# coding utf-8

import requests

from grandPyBotApp.api_wikiMedia import ApiWikiMedia

openclassrooms = ApiWikiMedia()


def test_ApiWikipedia(monkeypatch):
    results = ""
    
    def mockApiWikipedia():
        return results

    monkeypatch.setattr(requests, 'get', mockApiWikipedia)
 
    assert openclassrooms.content == ''

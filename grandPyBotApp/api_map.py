#! /usr/bin/env python3
# coding utf-8

from flask import request

from config import apiKeyMap

class ApiMap:
    def __init__(self, keyWord:str) -> str:
        self.urlMap = f"https://maps.googleapis.com/maps/api/geocode/json?address={keyWord}&key={apiKeyMap}"
        self.adress = self.get_adress()
        self.gps = self.get_gps()
    
    def get_adress(self):
        request.args.get(self.urlMap)
    
    def get_gps(self):
        pass
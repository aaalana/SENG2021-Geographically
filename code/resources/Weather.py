from flask_restful import Resource, Api
from flask import Flask, request, render_template, jsonify
import json, requests

APIKEY = 'OTgxMDg5ZDc1M2MyMjhmYjQwNTFlMz'

class Weather(Resource):
    def getWeather(locationID):
        url = 'https://api.willyweather.com.au/v2/{APIKEY}/locations/{locationID}/weather.json?forecasts=weather'.format(APIKEY = APIKEY, locationID=locationID)
        response = requests.get(url)
        res = json.loads(response.text)
        print(res)
        return res

    def getLocationID(locationstr):
        locationstr.replace(" ", "+")
        url = 'https://api.willyweather.com.au/v2/{APIKEY}/search.json?query={locationstr}&limit=1'.format(APIKEY=APIKEY,locationstr=locationstr)
        response = requests.get(url)
        res = json.loads(response.text)
        print(res)
        return res

id = Weather.getLocationID("Wollongong")[0]["id"]
weather = Weather.getWeather(id)
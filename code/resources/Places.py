from flask_restful import Resource, Api
from flask import Flask, request, render_template

import requests, json, geocoder

APIKEY = 'AIzaSyAFkE9C-jZGN-bocvETUHsJFm-F0cEhrVE'

class Places(Resource):
    def get(self):
        data = findRestaurant(getCurrentLocation())
        return data

#find restaurants within 1000 of a location
#ideally this would show restaurants within 5 minute drive of a route
def findRestaurant (loc):
    radius = 1000
    lat, lng = loc
    type = "restaurant"
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type={type}&key={APIKEY}".format(lat = lat, lng = lng, radius = radius, type = type,APIKEY = APIKEY)
    print(url)
    response = requests.get(url)
    res = json.loads(response.text)
    #prints out info in a simplified format
    for result in res["results"]:
        info = ";".join(map(str,[result["name"],result["geometry"]["location"]["lat"],result["geometry"]["location"]["lng"],result.get("rating",0),result["place_id"]]))
        print(info)
    return res

#returns locations of the first page of google for sydney tourist attractions
def findPointsOfInterest():
    location = "sydney"
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={location}+point+of+interest&language=en&key={APIKEY}".format(location=location, APIKEY=APIKEY)
    response = requests.get(url)
    res = json.loads(response.text)
    for result in res["results"]:
        print(result["name"])
    return res["results"][0]

#get current location
def getCurrentLocation():
    g = geocoder.ip('me')
    lat = str(g.latlng[0])
    lng = str(g.latlng[1])
    return lat, lng

def getPhotoId(location):
    print(location["photos"][0]["photo_reference"])
    return location["photos"][0]["photo_reference"]

def getPhotoLocation(refID):
    width = 400
    url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth={width}&photoreference={refID}&key={APIKEY}" 


print(getCurrentLocation())
findRestaurant(getCurrentLocation())
findPointsOfInterest()
id = getPhotoId(findPointsOfInterest())
getPhotoLocation(id)
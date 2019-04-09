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
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={location}+points+of+interest&language=en&key={APIKEY}".format(location=location, APIKEY=APIKEY)
        response = requests.get(url)
        res = json.loads(response.text)
        for result in res["results"]:
            print(result["name"])
        print(res["results"])
        return res["results"]

    #get current location
    def getCurrentLocation():
        g = geocoder.ip('me')
        lat = str(g.latlng[0])
        lng = str(g.latlng[1])
        return lat, lng

    def getPhoto(location):
        refID = location["photos"][0]["photo_reference"]
        width = 400
        url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth={width}&photoreference={refID}&key={APIKEY}".format(width = width, refID = refID, APIKEY = APIKEY) 
        print(url)
        return url

    def getPlacesInfo(locationstr):
        locationstr = locationstr.replace(' ','%20' )
        
        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={locationstr}&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key={APIKEY}"
        print(url)
    def getPhotoRecs(locations):
        
        lst = []
        k = 0
        for pn in locations:
            k = k + 1
            if k == 1:
                continue
            if k == 10:
                break
            d = {}
            refID =pn["photos"][0]["photo_reference"]
            width = 1000
            url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth={width}&photoreference={refID}&key={APIKEY}".format(width = width, refID = refID, APIKEY = APIKEY) 
            d['src'] = url
            lst.append(d)
        print(lst)
        return json.dumps(lst)

#print(getCurrentLocation())
#findRestaurant(getCurrentLocation())
#Places.findPointsOfInterest()
locations = Places.findPointsOfInterest()
Places.getPhotoRecs(locations)
    #print(location["photos"][0]["photo_reference"])
#id = getPhotoId(findPointsOfInterest())
#getPhotoLocation(id)
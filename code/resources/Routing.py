from flask_restful import Resource, Api
from flask import Flask, request, render_template, jsonify
import json, requests

APIKEY = 'AIzaSyAFkE9C-jZGN-bocvETUHsJFm-F0cEhrVE'

class Route(Resource):
    def findRouteInfo(start, end):
        #start = "Bridgewater, Sa, Australia"
        #finish = "Stirling, SA, Australia"
        print("The following should either be id or coords")
        print(start)
        if isinstance(start, tuple):
            start = str(start[0]+','+start[1]) 
            url = "https://maps.googleapis.com/maps/api/directions/json?origin={start}&destination=place_id:{end}&key={APIKEY}".format(start = start, end = end, APIKEY=APIKEY)
        else:
            url = "https://maps.googleapis.com/maps/api/directions/json?origin=place_id:{start}&destination=place_id:{end}&key={APIKEY}".format(start = start, end = end, APIKEY=APIKEY)
        print(start)
        print("REEEEEEEEEEEEEEEE")
        print(end)
        response = requests.get(url)
        res = json.loads(response.text)

        print(res["routes"][0]["legs"][0]["start_address"] + " to " + res["routes"][0]["legs"][0]["end_address"] +" Distance: " + res["routes"][0]["legs"][0]["distance"]["text"] + " Duration" +  res["routes"][0]["legs"][0]["duration"]["text"])
        #return res
        #print(res["routes"]["legs"]["start_address"])
            #print(routes["legs"]["start_address"] + routes["legs"]["end_address"] + routes["legs"]["distance"]["text"])
        data = {"start": res["routes"][0]["legs"][0]["start_address"], "end": res["routes"][0]["legs"][0]["end_address"],"dis": res["routes"][0]["legs"][0]["distance"]["text"], "time": res["routes"][0]["legs"][0]["duration"]["text"], "timesec": res["routes"][0]["legs"][0]["duration"]["value"]}
        return data

#Route.findRouteInfo("Bridgewater, Sa, Australia", "Stirling, SA, Australia")
import json, requests
import googlemaps

APIKEY = 'AIzaSyAFkE9C-jZGN-bocvETUHsJFm-F0cEhrVE'

def findRoute(start, finish):
    #start = "Bridgewater, Sa, Australia"
    #finish = "Stirling, SA, Australia"

    url = "https://maps.googleapis.com/maps/api/directions/json?origin={start}&destination={finish}&key={APIKEY}".format(start = start, finish = finish, APIKEY=APIKEY)
    response = requests.get(url)
    res = json.loads(response.text)

    print(res["routes"][0]["legs"][0]["start_address"] + " to " + res["routes"][0]["legs"][0]["end_address"] +" Distance: " + res["routes"][0]["legs"][0]["distance"]["text"] + " Duration" +  res["routes"][0]["legs"][0]["duration"]["text"])
    #print(res["routes"]["legs"]["start_address"])
        #print(routes["legs"]["start_address"] + routes["legs"]["end_address"] + routes["legs"]["distance"]["text"])    

findRoute("Bridgewater, Sa, Australia", "Stirling, SA, Australia")
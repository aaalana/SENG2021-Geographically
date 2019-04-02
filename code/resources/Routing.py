import json, requests
import googlemaps

APIKEY = 'AIzaSyAFkE9C-jZGN-bocvETUHsJFm-F0cEhrVE'

def findRoute(start, finish):
    #start = "Bridgewater, Sa, Australia"
    #finish = "Stirling, SA, Australia"

    url = "https://maps.googleapis.com/maps/api/directions/json?origin={start}&destination={finish}&key={APIKEY}".format(start = start, finish = finish, APIKEY=APIKEY)
    response = requests.get(url)
    res = json.loads(response.text)

    for result in res["routes"]:
        info = ";".join(map(str,[result["legs"]["start_address"]["end_address"],result["legs"]["distance"]["text"]]))
        print(info)

findRoute("Bridgewater, Sa, Australia", "Stirling, SA, Australia")
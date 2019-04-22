### Import dependancies/libraries
from flask import Flask, render_template
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
from resources.Places import *
from resources.Routing import *
from resources.parse import *
from resources.Weather import *
from resources.Music import *
from pymongo import MongoClient

### Import resources
from resources.users import Users

### Set up/connect to the Mongo Database
client = MongoClient("mongodb://localhost:27017/")
db = client.geographicallyDB
users = db.users

### Set 'flask' environment settings
app = Flask(__name__)
api = Api(app)
app.config.from_object(__name__)

# enable CORS
CORS(app)

route = [
    {
        'start': Places.getCurrentLocation(),
        'startID': Places.getCurrentLocation(),
        'end': "Canberra",
        'endID': Places.getPlacesID("Canberra")["candidates"][0]["place_id"]
    }
]
#we should get a json returning from the other functions and call it from here


recommendations = Places.findPointsOfInterest()
locationphotos = Places.getPhotoRecs(recommendations)
print(locationphotos)
locations = json.loads(locationphotos)
#print(findRoute)
class Recommendations(Resource):
    def get(self):
        return locations
        
class Routing(Resource):
    def get(self):
        print("dist")
        print(route)
        if not route[0]['start']:
            print(Places.getCurrentLocation())
            findRoute = Route.findRouteInfo(Places.getCurrentLocation(), route[0]['endID'])
        else:
            print("start id")
            print(route[0]['startID'])
            findRoute = Route.findRouteInfo(route[0]['startID'], route[0]['endID'])
        return jsonify(findRoute)        
    def put(self,start,end):
        findRoute = Route.findRouteInfo(start, end)
        return findRoute

class LocSummary(Resource):
    def get(self):
        summary = Summary.getPlaceSummary(route[0]['end'])
        return summary

class DestinationPhoto(Resource):
    def get(self):
        location = route[0]['end']
        print(location)
        info = Places.getPlacesInfo(location)
        print(info)
        return Places.getPhoto(info)

class CurrentLocation(Resource):
    def get(self):
        lat,lng = Places.getCurrentLocation()
        print(lat)
        print(lng)

        return jsonify( { 
            'lat': lat,
            'lng': lng
        })

class Location(Resource):
    def get(self):
        print('hi')
        print(route)
        return jsonify({
        'status': 'success',
        'location': route
        })
    def post(self):
        location = {'start':'help', 'dest' : 'end'}
        location = request.get_json()
        route[0]['start'] = location['start']
        route[0]['end'] = location['end']
        print("LOCATION")
        print(route[0]['end'])
        if route[0]['start']:
            route[0]['startID'] = Places.getPlacesID(location['start'])["candidates"][0]["place_id"]
        route[0]['endID'] = Places.getPlacesID(location['end'])["candidates"][0]["place_id"]
        print(route[0]['endID'])
        summary = Summary.getPlaceSummary(location["end"])
        print(summary)
        return location

class LocWeather(Resource):
    def get(self):
        locationID = Weather.getLocationID(route[0]['end'])[0]["id"]
        weather = Weather.getWeather(locationID)
        return weather

class Spotify(Resource):
    def get(self):
        music = Music.searchPlaylist(route[0]['end'])
        print(music)
        return music

api.add_resource(Recommendations, '/recommendation')
api.add_resource(Routing, '/trips')
api.add_resource(LocSummary, '/trips/summary')
api.add_resource(DestinationPhoto, '/trips/photo')
api.add_resource(Location, '/location')
api.add_resource(CurrentLocation, '/current')
api.add_resource(LocWeather, '/trips/weather')
api.add_resource(Spotify, '/trips/music')
@app.route('/')
def test_page():
    return Recommendations

@app.route('/location')
def sendInfo():
    print("test")
    details = request.get_json()
    print(details["end"])
    summary = Summary.getPlaceSummary("Canberra")
    print(details)
    print(summary)
    return jsonify(details)


### Add the Flask_RESTful resources here
api.add_resource(Users, '/Users')

### Start the server, (called through 'serverStart' script)
if __name__ == '__main__':
    app.run()

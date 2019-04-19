### Import dependancies/libraries
from flask import Flask, render_template
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
from resources.Places import *
from resources.Routing import *
<<<<<<< HEAD
from resources.parse import *
=======
from pymongo import MongoClient
>>>>>>> frontBackConnect

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
        'end': "Canberra"
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
        print(Places.getCurrentLocation())
        if not route[0]['start']:
            findRoute = Route.findRouteInfo(Places.getCurrentLocation(), route[0]['end'])
        else:
            findRoute = Route.findRouteInfo(route[0]['start'], route[0]['end'])
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
        summary = Summary.getPlaceSummary(location["end"])
        print(summary)
        return location

api.add_resource(Recommendations, '/recommendation')
api.add_resource(Routing, '/trips')
api.add_resource(LocSummary, '/trips/summary')
api.add_resource(DestinationPhoto, '/trips/photo')
api.add_resource(Location, '/location')
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

### Import dependancies/libraries
from flask import Flask, render_template
from flask_restful import reqparse, abort, Api, Resource
from resources.Places import *
from resources.Routing import *
from pymongo import MongoClient

### Import resources
from resources.users.py import Users

### Set up/connect to the Mongo Database
client = MongoClient("mongodb://localhost:27017/")
db = client.geographicallyDB
users = db.users

### Set 'flask' environment settings
app = Flask(__name__)
api = Api(app)

#we should get a json returning from the other functions and call it from here
start = "Bridgewater, Sa, Australia"
end = "Stirling, SA, Australia"

recommendations = Places.findPointsOfInterest()
findRoute = Route.findRouteInfo(start, end)
class Recommendations(Resource):
    def get(self):
        return recommendations
        
class Routing(Resource):
    def get(self):
        return findRoute        

api.add_resource(Recommendations, '/recommendation')
api.add_resource(Routing, '/trips')
@app.route('/')
def test_page():
    return render_template("index.html")

### Add the Flask_RESTful resources here
api.add_resource(Users, '\Users')

### Start the server, (called through 'serverStart' script)
if __name__ == '__main__':
    app.run()

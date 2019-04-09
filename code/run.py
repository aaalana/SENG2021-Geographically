from flask import Flask, render_template
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
from resources.Places import *
from resources.Routing import *
from resources.parse import *

app = Flask(__name__)
api = Api(app)
app.config.from_object(__name__)

# enable CORS
CORS(app)


#we should get a json returning from the other functions and call it from here
start = "Sydney"
end = "Canberra"

recommendations = Places.findPointsOfInterest()
findRoute = Route.findRouteInfo(start, end)
locationphotos = Places.getPhotoRecs(recommendations)
summary = Summary.getPlaceSummary(end)
#photo = 
print(summary)
print(locationphotos)
locations = json.loads(locationphotos)
print(findRoute)
class Recommendations(Resource):
    def get(self):
        return locations
        
class Routing(Resource):
    def get(self):
        return findRoute        
    def put(self,start,end):
        findRoute = Route.findRouteInfo(start, end)
        return findRoute

class Summary(Resource):
    def get(self):
        return summary

class DestinationPhoto(Resource):
    def get(self):
        return photo


        return summary
api.add_resource(Recommendations, '/recommendation')
api.add_resource(Routing, '/trips')
api.add_resource(Summary, '/trips/summary')
@app.route('/')
def test_page():
    return Recommendations

if __name__ == '__main__':
    app.run()

### Import dependancies/libraries
from flask import Flask
from flask_restful import Api, Resource
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

@app.route('/')
def test_page():
    return "Now we just need the whole finished project (Geographically) to put on the server..."

### Add the Flask_RESTful resources here
api.add_resource(Users, '\Users')

### Start the server, (called through 'serverStart' script)
if __name__ == '__main__':
    app.run()

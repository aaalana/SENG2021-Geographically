### Import dependancies/libraries
from flask import Flask, request, abort, jsonify, url_for
from flask_restful import Api, Resource
import pymongo

### Import resources
from resources.users.py import Users

### Set up/connect to the Mongo Database
client = MongoClient("mongodb://localhost:27017/")
db = client.geographically_DB
users = db.users

### Set 'flask' environment settings
app = Flask(__name__)
api = Api(app)

@app.route('/')
def test_page():
    return "Now we just need the whole finished project (Geographically) to put on the server..."



@app.route('/api/users', methods = ['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400) # missing arguments
    myquery = { "username": username }
    mydoc = mycol.find(myquery)
    if mydoc is not None:
        abort(400) # existing user
    user = User(username = username)
#    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({ 'username': user.username }), 201, {'Location': url_for('get_user', id = user.id, _external = True)}

### Add the Flask_RESTful resources here
api.add_resource(Users, '\Users')

### Start the server, (called through 'serverStart' script)
if __name__ == '__main__':
    app.run()

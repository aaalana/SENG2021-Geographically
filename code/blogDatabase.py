from flask import Flask, jsonify, request, json
#from flask_restful import Resource, Api
from flask_cors import CORS
from flask_pymongo import PyMongo
from pymongo import MongoClient

# INCOMPLETE MONGO DATABASE - NOT WORKING -> firebase used instead

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/blog'
mongo = PyMongo(app)
CORS(app)
#api = Api(app)


# MongoClient object connected to localhost
#client = MongoClient('localhost', 5000)

# can also write as db = client.pymongo_test
# instance of mongo client
#db = client['pymongo_test']

# collection name
#posts = db.posts

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
@app.route('/')
def index():
    return 'Homepage'

@app.route('/blog', methods=['GET'])
def addPost():
        #headers={"content-type":["application/json",]}
        posts = mongo.db.post
        title = request.get_json()['title']
        content = request.get_json()['content']
        date = request.get_json()['date']
        #blogPost = {'title': title.get('title'), 'content': content.get('content'), 'date': date.get('date')}
        blogPost = {'title': title, 'content': content, 'date': date}
        result = posts.insert(blogPost) 
        #result = posts.insert_one(blogPost)
        print(result)
        
        return jsonify({ 'result' : result })
        
'''
class blog(Response):
    def get(self):
        # insert response.data into your collection
        result = posts.insert_one(Response)
        print('One post: {0}'.format(result.inserted_id))

        return result
'''

#api.add_resource(blog, '/')

if __name__ == '__main__':
    app.run(debug=True)
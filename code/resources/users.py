from flask import Flask, request
from flask_restful import Resource, Api


class Users(Resource):
    def get(self):
        return "users data here, should be 'API'-i-fied"

    def get(self, id):
        return "users data here, should be 'API'-i-fied"

    def post(self, id):
        pass 

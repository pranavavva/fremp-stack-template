from flask import Flask, jsonify
from flask_mongoengine import MongoEngine
from flask_restful import Api, Resource
import os

from mongoengine.fields import StringField

app = Flask(__name__, static_url_path="/", static_folder="../frontend/build")
api = Api(app)

app.config["MONGODB_SETTINGS"] = {
    "db": os.environ.get("MONGODB_DB"),
    "host": os.environ.get("MONGODB_HOST"),
    "port": int(os.environ.get("MONGODB_PORT")),
    "username": os.environ.get("MONGODB_USERNAME"),
    "password": os.environ.get("MONGODB_PASSWORD"),
}

db = MongoEngine(app)

@app.route("/")
def home():
    return app.send_static_file("index.html")


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file("index.html")

class HelloWorldMonogo(db.Document):
    text = StringField(required=True)
    meta = {"collection": "hello_world"}


class HelloWorldAPI(Resource):
    def get(self):
        return jsonify(HelloWorldMonogo.objects.first())


api.add_resource(HelloWorldAPI, "/api/hello")

from flask import Flask
from flask_restful import Api
from resources.map import Map


app = Flask(__name__)
api = Api(app)
api.add_resource(Map, "/map")


if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

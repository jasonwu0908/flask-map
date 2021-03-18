from flask_restful import Resource, reqparse
from flask import redirect


parser = reqparse.RequestParser()
parser.add_argument('longitude', type=float)
parser.add_argument('latitude', type=float)


class Map(Resource):

    def get(self):
        args = parser.parse_args()
        longitude = args.get('longitude', 0)
        latitude = args.get('latitude', 0)
        url=f"https://www.google.com/maps/place/{latitude},{longitude}"
        return redirect(url, code=302)

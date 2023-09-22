from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

person_args=reqparse.RequestParser()
person_args.add_argument("name")
person_args.add_argument("age",type=int)
person_args.add_argument("gender")

class person(Resource):
    def get(self):
        return "hello"
    def post(self):
        args=person_args.parse_args()
        return args

class FlutterNewsApp(Resource):
    def get(self):
        return 200

api.add_resource(person,"/person")
api.add_resource(FlutterNewsApp,"/FlutterNewsApp")

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')

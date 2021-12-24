from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class Add(Resource):
    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("num1", type=int)
        parser.add_argument("num2", type=int)

        num1 = parser.parse_args().get("num1")
        num2 = parser.parse_args().get("num2")

        return num1 + num2


class Subtract(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("num1", type=int)
        parser.add_argument("num2", type=int)

        num1 = parser.parse_args().get("num1")
        num2 = parser.parse_args().get("num2")

        return num1 - num2


class Multiply(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("num1", type=int)
        parser.add_argument("num2", type=int)

        num1 = parser.parse_args().get("num1")
        num2 = parser.parse_args().get("num2")

        return num1 * num2

    
class Divide(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("num1", type=int)
        parser.add_argument("num2", type=int)

        num1 = parser.parse_args().get("num1")
        num2 = parser.parse_args().get("num2")

        return num1 / num2

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
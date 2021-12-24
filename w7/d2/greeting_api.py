from flask import Flask, jsonify
from flask_restful import  Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class Greet(Resource):
    
    def get(self):
        parser = reqparse.RequestParser()

        parser.add_argument("name", type=str)

        name = parser.parse_args().get("name")

        if name:
            greeting = f"Hello {name}!"
        else:
            greeting = "Hello!"

        return jsonify(greeting=greeting)


api.add_resource(Greet, "/greet")


# Run script only if file is called directly (not imported as a module)
if __name__ == "__main__":
    app.run(debug=True, port=8000)
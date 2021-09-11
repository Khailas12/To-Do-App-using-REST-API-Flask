from flask import Flask, request
from flask_restful import Resource, Api, reqparse,fields, marshal_with

# CRUD Resource is used in here

app = Flask(__name__)
api = Api(app)
 
 
to_do = {}

class ToDoSimple(Resource):
    def get(self, to_do_id):
        return {to_do_id: to_do[to_do_id]}
    
    def put(self, to_do_id):
        to_do[to_do_id] = request.form['data']
        return {to_do_id: to_do[to_do_id]}
    
api.add_resource(ToDoSimple, '/<string:to_do_id>')

class Todo1(Resource):
    def get(self):
        return {'task', 'Hello world'}

class Todo2(Resource):
    def get(self):
        return {'talk', 'Hello world'}, 201
    
class Todo3(Resource):
    def get(self):
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}


# Flask-RESTful has built-in support for request data validation using a library similar to argparse.
parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate to change the resource')
# args = parser.parse_args(strict=True)   # Calling parse_args with strict=True ensures that an error is thrown if the request includes arguments your parser does not define.
# Unlike the argparse module, reqparse.RequestParser.parse_args() returns a Python dictionary instead of a custom data structure.
    
resourse_fields = {
    "task": fields.String,
    "uri": fields.Url('todo_ep')
}

class ToDoDo(object):
    def __init__(self, to_do_id, task):
        self.to_do_id = to_do_id
        self.task = task
        self.status = 'active'
        
class ToDo(Resource):
    @marshal_with(resourse_fields)  # marshal_with -> A decorator that apply marshalling to the return values of your methods. 
    def get(self, **kwargs):
        return ToDoDo(to_do_id='my_todo', task='Remember the milk')


if __name__ == "__main__":
    app.run(port=5000, debug=True)
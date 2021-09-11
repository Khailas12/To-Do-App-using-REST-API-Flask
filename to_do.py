from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)


TODO = {
    "todo1": {"task": "build an API"}, 
    "todo2": {"task": "????"},
    "todo3": {"task": "profit"},
}

def abort_todo(todo_id):
    if todo_id not in TODO:
        abort(404, message="Todo {} doesn't exist".format(todo_id))
    
parser = reqparse.RequestParser()
parser.add_argument('task')
# the processing of a piece of python program and converting these codes into machine language,  
# In other words, the interpreter component that breaks data into smaller elements for easy translation into another language


class ToDo(Resource):
    def get(self, todo_id):
        abort_todo(todo_id)
        return TODO[todo_id]
    
    def delete(self, todo_id):
        abort_todo(todo_id)
        del TODO[todo_id]
        return "", 201
    

class ToDoList(Resource):
    def get(self):
        return TODO
    
    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODO.keys()).lstrip('todo')) + 1
        todo_id = 'todo%oi' % todo_id
        # String lstrip() method returns a copy of the string with leading characters removed 
        
        TODO[todo_id] = {'task': args['task']}
        return TODO[todo_id], 201
    
api.add_resource(ToDoList, '/todo')
api.add_resource(ToDo, '/todo/<todo_id>')

if __name__ == "__main__":
    app.run(debug=True)
    
    
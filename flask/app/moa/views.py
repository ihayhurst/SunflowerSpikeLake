from flask import Blueprint
from flask_restful import Api, Resource
import cx_Oracle

moa = Blueprint('moa', __name__)
api = Api(moa)

"""
with cx_Oracle.connect(userName, password, "dbhost.example.com/orclpdb1",
            encoding="UTF-8") as connection:
    cursor = connection.cursor()
    cursor.execute("insert into SomeTable values (:1, :2)",
            (1, "Some string"))
    connection.commit() 
"""
class TodoItem(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}

@moa.route("/")
def moa_home():
    return "<h1>API Home</h1>"

api.add_resource(TodoItem, '/todos/<int:id>')

from flask import Blueprint, Response
from flask import current_app as app
from flask_restful import Api, Resource
import cx_Oracle
import markdown
import os
#from .. import db

moa = Blueprint('moa', __name__)
api = Api(moa)

def dbGetConn():
    dbhost = app.config['DATABASE_HOST']
    dbport = app.config['DATABASE_PORT']
    dbname = app.config['DATABASE_NAME']
    dbuser = app.config['DATABASE_USER']
    dbpw = app.config['DATABASE_PASSWORD']
    conn_str = f"{dbuser}/{dbpw}@//{dbhost}:{dbport}/{dbname}"
    conn = cx_Oracle.connect(conn_str)
    return conn

def getData(sql):
    conn = dbGetConn()
    curr = conn.cursor()
    curr.execute(sql)
    data = curr.fetchall()
    jsonData = [dict(zip([key[0] for key in curr.description], row)) for row in data]
    curr.close()
    conn.close()
    return (jsonData if jsonData else None)


@moa.route('/')
def moa_home():
    """Present some documentation"""

    # Open the README file
    with open(os.path.join(moa.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)


@moa.route('/wibble')
def wibble():
    #data = moa.config'[DATABASE_HOST']
    data = "some data"
    return f"<h4>wibble: </h4>{data}"

class Entity(Resource):
    def get(self, id):
        sql = f"select * from MOA_ENTITY where entity_id={id}"
        data  = getData(sql)
        return data, 201

class Entitys(Resource):
    def get(self):
        sql = f"select * from MOA_ENTITY"
        data  = getData(sql)
        return data, 201

api.add_resource(Entity, '/entity/<int:id>')
api.add_resource(Entitys, '/entity')

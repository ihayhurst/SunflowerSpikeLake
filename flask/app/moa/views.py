from flask import  Blueprint
from flask import current_app as app
from flask_restful import Api, Resource
from .. import db
import cx_Oracle

moa = Blueprint('moa', __name__)
api = Api(moa)

@moa.route("/")
def moa_home():
    dsn = cx_Oracle.makedsn(app.config['DATABASE_HOST'],
                            app.config['DATABASE_PORT'],
                            service_name="APEXRDP2")
    id = 222

    #conn_str = f"{app.config['DATABASE_USER']}, {app.config['DATABASE_PASSWORD']}, {dsn}"
    conn_str ="SCO_MOA_ONTOLOGY/sc0_m04_0n70logy@//deawdoraappp001.c0teethmpf9v.eu-central-1.rds.amazonaws.com:1530/APEXRDP2"
    print(conn_str)
    sql = f"select * from MOA_ENTITY where entity_id={id}"
    conn = cx_Oracle.connect(conn_str)
    curr = conn.cursor()
    curr.execute(sql)
    data = curr.fetchall()
    curr.close()
    conn.close()
    return f"return: {data}"
    #return f"<h1>API Home</h1>{conn_str}"
"""
class Entity(Resource):
    dsn = cx_Oracle.makedsn(app.config['DATABASE_HOST'],
                            app.config['DATABASE_PORT'],
                            app.config['DATABASE_NAME'])

    conn_str = f"{app.config['DATABASE_USER']}, {app.config['DATABASE_PASSWORD']}, {dsn}, encoding='UTF-8'"
    def get(self, id):

api.add_resource(Entity, '/entity/<int:id>')
"""

from flask import Blueprint, Response
from flask import current_app as app
from flask_restful import Api, Resource
import cx_Oracle
import markdown
import os

moa = Blueprint("moa", __name__)
api = Api(moa)


def dbGetConn():
    dbhost = app.config["DATABASE_HOST"]
    dbport = app.config["DATABASE_PORT"]
    dbname = app.config["DATABASE_NAME"]
    dbuser = app.config["DATABASE_USER"]
    dbpw = app.config["DATABASE_PASSWORD"]
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
    return jsonData if jsonData else None


@moa.route("/")
def moa_home():
    """Present some documentation"""

    # Open the README file
    with open(os.path.join(moa.root_path) + "/README.md", "r") as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        md = markdown.markdown(content, extensions=["tables", "fenced_code"])
        return md


class Entity(Resource):
    def get(self, id=None):
        if id is not None:
            sql = f"select * from MOA_ENTITY where entity_id={id}"
        else:
            sql = f"select * from MOA_ENTITY"
        data = getData(sql)
        return data, 201


class Triple(Resource):
    def get(self, tripleid=None, subjectid=None, predicateid=None, objectid=None):
        if tripleid is not None:
            sql = f"select * from MOA_TRIPLE where triple_id={tripleid}"
        elif subjectid is not None:
            sql = f"select * from MOA_TRIPLE where subject_id={subjectid}"
        elif predicateid is not None:
            sql = f"select * from MOA_TRIPLE where predicate_id={predicateid}"
        elif objectid is not None:
            sql = f"select * from MOA_TRIPLE where object_id={predicateid}"
        else:
            sql = f"select * from MOA_TRIPLE"
        data = getData(sql)
        return data, 201


api.add_resource(Entity, "/entity/<int:id>", endpoint="entity")
api.add_resource(Entity, "/entity", endpoint="entitys")
api.add_resource(Triple, "/triple/triple/<int:tripleid>", endpoint="tripleid")
api.add_resource(Triple, "/triple/subject/<int:subjectid>", endpoint="subjectid")
api.add_resource(Triple, "/triple/predicate/<int:predicateid>", endpoint="predicateid")
api.add_resource(Triple, "/triple/object/<int:objectid>", endpoint="objectid")
api.add_resource(Triple, "/triple/<int:tripleid>", endpoint="triple")
api.add_resource(Triple, "/triple", endpoint="triples")

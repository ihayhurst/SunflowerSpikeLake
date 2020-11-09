from flask import Blueprint
from flask import current_app as app
from flask_restful import Api, Resource, reqparse
import json
import datetime
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


def dump_date(thing):
    if isinstance(thing, datetime.datetime):
        return thing.isoformat()
    return thing


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
            sql = "select * from MOA_ENTITY"
        data = getData(sql)
        # set default handler to dump_date if there is a date object
        data = json.dumps(data, default=dump_date)
        data = json.loads(data)
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
            sql = f"select * from MOA_TRIPLE where object_id={objectid}"
        else:
            sql = "select * from MOA_TRIPLE"
        data = getData(sql)
        return data, 201


class Evidence(Resource):
    def get(self, evidenceid=None, evidenceTripleid=None):
        if evidenceid is not None:
            sql = f"select * from MOA_EVIDENCE where evidence_id={evidenceid}"
        elif evidenceTripleid is not None:
            sql = f"select * from MOA_EVIDENCE where triple_id={evidenceTripleid}"
        else:
            sql = "select * from MOA_EVIDENCE"
        data = getData(sql)
        return data, 201


class Group(Resource):
    def get(self, groupid=None, entityid=None):
        if groupid is not None:
            sql = f"select * from MOA_GROUP where MOA_GROUP_ID={groupid}"
        elif entityid is not None:
            sql = f"select * from MOA_GROUP where ENTITY_ID={entityid}"
        else:
            sql = "select * from MOA_GROUP"
        data = getData(sql)
        return data, 201


class SpeciesProtein(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("species", type=str, location="args")
        self.reqparse.add_argument("uniprot", type=str, location="args")
        super(SpeciesProtein, self).__init__()

    def get(self, sprotid=None, entityid=None):
        args = self.reqparse.parse_args()
        if sprotid is not None:
            sql = (
                f"select * from MOA_SPECIES_PROTEIN where SPECIES_PROTEIN_ID={sprotid}"
            )
        elif entityid is not None:
            sql = f"select * from MOA_SPECIES_PROTEIN where ENTITY_ID={entityid}"
        elif args["species"] is not None:
            speccode = args["species"]
            sql = f"select * from MOA_SPECIES_PROTEIN where SPECIES_CODE='{speccode}'"
        elif args["uniprot"] is not None:
            uniprot = args["uniprot"]
            sql = f"select * from MOA_SPECIES_PROTEIN where UNIPROT_CODE='{uniprot}'"
        else:
            sql = "select * from MOA_SPECIES_PROTEIN"
        data = getData(sql)
        return data, 201


class EntityLink(Resource):
    def get(self, elid=None, entityid=None):
        if elid is not None:
            sql = f"select * from MOA_ENTITY_LINK where ID={elid}"
        elif entityid is not None:
            sql = f"select * from MOA_ENTITY_LINK where ENTITY_ID={entityid}"
        else:
            sql = "select * from MOA_ENTITY_LINK"
        data = getData(sql)
        return data, 201


# Resources
# Entity
api.add_resource(Entity, "/entity/<int:id>", endpoint="entity")
api.add_resource(Entity, "/entity", endpoint="entitys")
# Triple
api.add_resource(Triple, "/triple", endpoint="triples")
api.add_resource(Triple, "/triple/<int:tripleid>", endpoint="triple")
api.add_resource(Triple, "/triple/triple/<int:tripleid>", endpoint="tripleid")
api.add_resource(Triple, "/triple/subject/<int:subjectid>", endpoint="subjectid")
api.add_resource(Triple, "/triple/predicate/<int:predicateid>", endpoint="predicateid")
api.add_resource(Triple, "/triple/object/<int:objectid>", endpoint="objectid")
# Evidence
api.add_resource(Evidence, "/evidence", endpoint="evidences")
api.add_resource(Evidence, "/evidence/<int:evidenceid>", endpoint="evidence")
api.add_resource(Evidence, "/evidence/evidence/<int:evidenceid>", endpoint="evidenceid")
api.add_resource(
    Evidence, "/evidence/triple/<int:evidenceTripleid>", endpoint="evidenceTripleid"
)
# Group
api.add_resource(Group, "/group", endpoint="groups")
api.add_resource(Group, "/group/<int:groupid>", endpoint="group")
api.add_resource(Group, "/group/group/<int:groupid>", endpoint="groupid")
api.add_resource(Group, "/group/entity/<int:entityid>", endpoint="entityid")
# SpeciesProtein
api.add_resource(SpeciesProtein, "/species-protein", endpoint="species-proteins")
api.add_resource(
    SpeciesProtein, "/species-protein/<int:sprotid>", endpoint="species-protein"
)
api.add_resource(
    SpeciesProtein,
    "/species-protein/species-protein/<int:sprotid>",
    endpoint="species-proteinid",
)
api.add_resource(
    SpeciesProtein, "/species-protein/entity/<int:entityid>", endpoint="sprentityid"
)
api.add_resource(SpeciesProtein, "/species-protein/species-code", endpoint="speccode")
api.add_resource(
    SpeciesProtein, "/species-protein/uniprot-code", endpoint="uniprotcode"
)
# EntityLink
api.add_resource(EntityLink, "/entity-link", endpoint="entitylinks")
api.add_resource(EntityLink, "/entity-link/<int:elid>", endpoint="entitylink")
api.add_resource(EntityLink, "/entity-link/entity-link/<int:elid>", endpoint="elid")
api.add_resource(
    EntityLink, "/entity-link/entity/<int:entityid>", endpoint="elentityid"
)

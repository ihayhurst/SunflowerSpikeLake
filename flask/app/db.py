from flask import current_app as app
import cx_Oracle

# Set up Oracle conn globally
class oracle_connection(object):

    def __init__(self,connection_string):
        self.connection_string = connection_string
        self.connector = None

    def __enter__(self):
        self.connector = cx_Oracle.connect(self.connection_string)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            self.connector.commit()
        else:
            self.connector.rollback()
            self.connector.close()
"""
with cx_Oracle.connect(userName, password, "dbhost.example.com/orclpdb1",
            encoding="UTF-8") as connection:
    cursor = connection.cursor()
    cursor.execute("insert into SomeTable values (:1, :2)",
            (1, "Some string"))
    connection.commit()
# select * from MOA_ENTITY where entity_id=222;
return f"DATABASE: {current_app.config['DATABASE_HOST']}"
def init_app(app):
    app.teardown_appcontext(close_db)
"""

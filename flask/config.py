class Config(object):
    DATABASE_HOST = "somehost"
    DATABASE_NAME = "dbname"
    DATABASE_PORT = 1530
    DATABASE_USER = "dbuser"
    DATABASE_PASSWORD = "secret_ pw"


class Production(Config):
    pass

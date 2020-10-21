class Config(object):
    """ Readonly database lookup user """

    DATABASE_HOST = "deawdoraappp001.c0teethmpf9v.eu-central-1.rds.amazonaws.com"
    DATABASE_NAME = "APEXRDP2"
    DATABASE_PORT = 1530
    DATABASE_USER = "SCO_MOA_ONTOLOGY"
    DATABASE_PASSWORD = "sc0_m04_0n70logy"


class Production(Config):
    pass

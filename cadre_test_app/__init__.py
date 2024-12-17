import sys

import fastjsonschema
from cadre import Cadre


class Cadre_Test_App(Cadre):

    def validate_query(self, schema):
        from cadre import request
        fastjsonschema.compile(schema)(request.json)


def serve():
    if len(sys.argv) != 2:
        print("Usage: %s config.ini")
        sys.exit(1)
    Cadre_Test_App(sys.argv[1]).serve()


def dump_routes():
    if len(sys.argv) != 2:
        print("Usage: %s config.ini")
        sys.exit(1)
    Cadre_Test_App(sys.argv[1]).dump_routes()

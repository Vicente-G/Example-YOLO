from flask import Request, Response
from jsonschema import ValidationError

from src.process import main


def response(req: Request) -> Response:
    try:
        body = main(req.get_json())
        return Response(body, status=200, mimetype="application/json")
    except (ValueError, ValidationError) as error:
        body = {"error": str(error)}
        return Response(body, status=400, mimetype="application/json")
    except KeyError as error:
        body = {"error": str(error)}
        return Response(body, status=500, mimetype="application/json")

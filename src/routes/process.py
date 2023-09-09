from flask import Request, Response, jsonify
from jsonschema import ValidationError
from ultralytics import YOLO

from src.process import main


def response(req: Request, model: YOLO) -> tuple[Response, int]:
    try:
        return jsonify(main(req.get_json(), model)), 200
    except (ValueError, ValidationError) as error:
        return jsonify({"error": str(error)}), 400
    except KeyError as error:
        return jsonify({"error": str(error)}), 500

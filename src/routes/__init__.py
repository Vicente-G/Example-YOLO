from flask import Flask, Response, request
from ultralytics import YOLO

from .process import response as process_response


def router(app: Flask, model: YOLO) -> Flask:
    @app.route("/status", methods=["GET"])
    def status() -> tuple[Response, int]:
        return Response(None), 200

    @app.route("/process", methods=["POST"])
    def process() -> tuple[Response, int]:
        return process_response(request, model)

    return app

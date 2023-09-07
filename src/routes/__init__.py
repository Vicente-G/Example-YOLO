from flask import Flask, Response, request

from .process import response as process_response


def router(app: Flask) -> Flask:
    @app.route("/status", methods=["GET"])
    def status() -> Response:
        return Response(None, status=200)

    @app.route("/process", methods=["POST"])
    def process() -> Response:
        return process_response(request)

    return app

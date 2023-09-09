from argparse import ArgumentParser

from flask import Flask
from ultralytics import YOLO

from src.config import PORT
from src.routes import router

MODEL_PATH = "./src/models/yolov8n.pt"

if __name__ == "__main__":
    model = YOLO(MODEL_PATH)
    parser = ArgumentParser()
    parser.add_argument("--debug", default=False, action="store_true")
    args, unknown = parser.parse_known_args()

    app = Flask(__name__)
    app = router(app, model)
    app.run(debug=args.debug, host="0.0.0.0", port=PORT)

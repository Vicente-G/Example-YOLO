from ultralytics import YOLO

from .numbers import get_classes, get_mids
from .tools import encode_as_b64, load_from_b64
from .validation import request_validate


def main(data: dict[str, str], model: YOLO) -> dict[str, str | list[int]]:
    payload = request_validate(data)
    img = load_from_b64(payload["image"])
    result = model.predict(img, device="cpu", conf=0.5)[0]
    annotations = encode_as_b64(result.plot())
    return {
        "image": annotations,
        "locs": get_mids(result.boxes.xyxy.numpy()),
        "classes": get_classes(result.boxes.cls.numpy()),
    }

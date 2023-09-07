import cv2

from .tools import encode_as_b64, load_from_b64
from .validation import request_validate


def main(data: dict[str, str]) -> dict[str, str]:
    payload = request_validate(data)
    img = load_from_b64(payload["image"])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    response = encode_as_b64(gray)
    return {"image": response}

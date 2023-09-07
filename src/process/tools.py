import base64

import cv2
import numpy as np


def load_from_b64(payload: str) -> np.uint8:
    decode = base64.b64decode(payload)
    arr = np.frombuffer(decode, np.uint8)
    mat = cv2.imdecode(arr, cv2.IMREAD_ANYCOLOR)
    return np.uint8(mat)


def encode_as_b64(img: np.uint8) -> str:
    ret, buffer = cv2.imencode(".jpg", img)
    if not ret:
        raise ValueError("Failed to encode image")
    encode = base64.b64encode(buffer)  # type: ignore[arg-type]
    return str(encode, "utf-8")

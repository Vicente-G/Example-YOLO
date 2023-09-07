import cv2
import numpy as np
from jsonschema import ValidationError
from pytest import fixture, raises

from src.process import encode_as_b64, load_from_b64, main


@fixture
def image():
    return np.uint8(cv2.imread("./test/data/img.jpg"))


@fixture
def b64(image):
    return encode_as_b64(image)


@fixture
def data(b64):
    return main({"image": b64})


def test_existence(data):
    assert "image" in data


def test_types_by_step(image, b64, data):
    assert isinstance(image, np.ndarray)
    assert isinstance(b64, str)
    assert isinstance(data["image"], str)


def test_image_is_gray(image, data):
    gray = load_from_b64(data["image"])
    local_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    assert gray.shape == local_gray.shape
    assert round(np.mean(gray / local_gray), 2) == 1.00


def test_error_on_validation():
    with raises(ValidationError) as error:
        main({"image": 123})
        assert error == "123 is not of type 'string'"

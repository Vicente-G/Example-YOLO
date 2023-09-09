import cv2
import numpy as np
from jsonschema import ValidationError
from pytest import fixture, raises
from ultralytics import YOLO

from src import MODEL_PATH
from src.process import encode_as_b64, main


@fixture
def image():
    return np.uint8(cv2.imread("./test/data/img.jpeg"))


@fixture
def b64(image):
    return encode_as_b64(image)


@fixture
def model():
    return YOLO(MODEL_PATH)


@fixture
def data(b64, model):
    return main({"image": b64}, model)


def test_existence(data):
    assert "image" in data


def test_types_by_step(image, b64, data):
    assert isinstance(image, np.ndarray)
    assert isinstance(b64, str)
    assert isinstance(data["image"], str)


def test_image_has_dog(data):
    detection = data["classes"]
    assert 16 in detection


def test_image_has_bicycle(data):
    detection = data["classes"]
    assert 1 in detection


def test_error_on_validation(model):
    with raises(ValidationError) as error:
        main({"image": 123}, model)
        assert error == "123 is not of type 'string'"

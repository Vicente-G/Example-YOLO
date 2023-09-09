import numpy as np


def get_mids(boxes: np._typing.NDArray[np.uint8]) -> list[int]:
    mids = np.uint8((boxes[:, :2] + boxes[:, 2:]) / 2)
    flattened = mids.flatten()
    return flattened.tolist()  # type: ignore[no-any-return]


def get_classes(boxes: np._typing.NDArray[np.uint8]) -> list[int]:
    flattened = boxes.flatten()
    return flattened.tolist()  # type: ignore[no-any-return]

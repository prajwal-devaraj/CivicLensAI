import numpy as np
from civiclens_perception.frame import CameraFrame
from civiclens_perception.preprocessing import VisionPreprocessor


def test_vision_preprocessor_resizes_and_converts_color():
    image = np.zeros((480, 640, 3), dtype=np.uint8)
    image[0, 0] = [255, 0, 0]

    frame = CameraFrame(
        source_id="test-camera",
        width=640,
        height=480,
        image=image,
    )

    processed = VisionPreprocessor().prepare(
        frame,
        target_width=320,
        target_height=320,
    )

    assert processed.shape == (320, 320, 3)
    assert processed.dtype == np.uint8

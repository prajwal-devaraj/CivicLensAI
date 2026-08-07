import numpy as np
from civiclens_perception.mock_vision_model import MockVisionModel
from civiclens_perception.prediction import VisionPrediction


def test_mock_vision_model_returns_detection():
    image = np.zeros((640, 640, 3), dtype=np.uint8)

    prediction = MockVisionModel().infer(image)

    assert isinstance(prediction, VisionPrediction)
    assert prediction.count == 1

    detection = prediction.detections[0]

    assert detection.label == "person"
    assert detection.confidence == 0.99
    assert detection.bounding_box.width == 200
    assert detection.bounding_box.height == 420

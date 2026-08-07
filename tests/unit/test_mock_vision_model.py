import numpy as np
from civiclens_perception.mock_vision_model import MockVisionModel
from civiclens_perception.prediction import VisionPrediction


def test_mock_vision_model_returns_prediction():
    image = np.zeros((640, 640, 3), dtype=np.uint8)

    prediction = MockVisionModel().infer(image)

    assert isinstance(prediction, VisionPrediction)
    assert prediction.label == "synthetic-scene"
    assert prediction.confidence == 1.0

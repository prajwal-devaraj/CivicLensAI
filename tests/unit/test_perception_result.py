import numpy as np
from civiclens_perception.bounding_box import BoundingBox
from civiclens_perception.detection import ObjectDetection
from civiclens_perception.events import PerceptionEvent
from civiclens_perception.prediction import VisionPrediction
from civiclens_perception.result import PerceptionResult


def test_perception_result_holds_event_image_and_prediction():
    event = PerceptionEvent(
        source="front-camera",
        modality="vision",
    )

    image = np.zeros((320, 320, 3), dtype=np.uint8)

    prediction = VisionPrediction(
        detections=(
            ObjectDetection(
                label="person",
                confidence=0.99,
                bounding_box=BoundingBox(
                    x_min=10,
                    y_min=20,
                    x_max=110,
                    y_max=220,
                ),
            ),
        )
    )

    result = PerceptionResult(
        event=event,
        image=image,
        prediction=prediction,
    )

    assert result.event == event
    assert result.image.shape == (320, 320, 3)
    assert result.prediction == prediction
    assert result.prediction.count == 1

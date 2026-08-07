from civiclens_perception.bounding_box import BoundingBox
from civiclens_perception.detection import ObjectDetection
from civiclens_perception.detection_filter import DetectionFilter
from civiclens_perception.prediction import VisionPrediction


def test_detection_filter_removes_low_confidence_detections():
    prediction = VisionPrediction(
        detections=(
            ObjectDetection(
                label="person",
                confidence=0.95,
                bounding_box=BoundingBox(10, 20, 100, 200),
            ),
            ObjectDetection(
                label="chair",
                confidence=0.30,
                bounding_box=BoundingBox(200, 100, 300, 250),
            ),
        )
    )

    filtered = DetectionFilter(minimum_confidence=0.5).apply(prediction)

    assert filtered.count == 1
    assert filtered.detections[0].label == "person"

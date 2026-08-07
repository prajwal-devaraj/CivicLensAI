from civiclens_perception.bounding_box import BoundingBox
from civiclens_perception.detection import ObjectDetection


def test_object_detection_holds_detection_data():
    detection = ObjectDetection(
        label="person",
        confidence=0.97,
        bounding_box=BoundingBox(
            x_min=10,
            y_min=20,
            x_max=110,
            y_max=220,
        ),
    )

    assert detection.label == "person"
    assert detection.confidence == 0.97
    assert detection.bounding_box.width == 100
    assert detection.bounding_box.height == 200

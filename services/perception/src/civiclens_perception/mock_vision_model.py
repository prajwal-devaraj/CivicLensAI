import numpy as np

from .bounding_box import BoundingBox
from .detection import ObjectDetection
from .prediction import VisionPrediction


class MockVisionModel:
    """Simple vision model used for development and tests."""

    def infer(self, image: np.ndarray) -> VisionPrediction:
        return VisionPrediction(
            detections=(
                ObjectDetection(
                    label="person",
                    confidence=0.99,
                    bounding_box=BoundingBox(
                        x_min=100,
                        y_min=80,
                        x_max=300,
                        y_max=500,
                    ),
                ),
            )
        )

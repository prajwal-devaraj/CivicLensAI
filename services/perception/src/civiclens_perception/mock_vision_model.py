import numpy as np

from .prediction import VisionPrediction


class MockVisionModel:
    """Simple vision model used for development and tests."""

    def infer(self, image: np.ndarray) -> VisionPrediction:
        return VisionPrediction(
            label="synthetic-scene",
            confidence=1.0,
        )

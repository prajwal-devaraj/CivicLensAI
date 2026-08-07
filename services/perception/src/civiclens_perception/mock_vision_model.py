import numpy as np


class MockVisionModel:
    """Simple vision model used for development and tests."""

    def infer(self, image: np.ndarray) -> dict[str, object]:
        return {
            "label": "synthetic-scene",
            "confidence": 1.0,
            "shape": image.shape,
        }

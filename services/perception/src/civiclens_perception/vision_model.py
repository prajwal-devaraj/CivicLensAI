from typing import Protocol

import numpy as np

from .prediction import VisionPrediction


class VisionModel(Protocol):
    """Contract for CivicLens vision inference models."""

    def infer(self, image: np.ndarray) -> VisionPrediction:
        """Run inference on a preprocessed image."""
        ...

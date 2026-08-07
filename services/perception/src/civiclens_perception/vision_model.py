from typing import Protocol

import numpy as np


class VisionModel(Protocol):
    """Contract for CivicLens vision inference models."""

    def infer(self, image: np.ndarray) -> dict[str, object]:
        """Run inference on a preprocessed image."""
        ...

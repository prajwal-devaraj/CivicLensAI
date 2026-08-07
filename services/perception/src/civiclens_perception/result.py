from dataclasses import dataclass

import numpy as np

from .events import PerceptionEvent
from .prediction import VisionPrediction


@dataclass(frozen=True, slots=True)
class PerceptionResult:
    """Output produced by the CivicLens perception pipeline."""

    event: PerceptionEvent
    image: np.ndarray
    prediction: VisionPrediction

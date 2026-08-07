from dataclasses import dataclass

import numpy as np

from .events import PerceptionEvent


@dataclass(frozen=True, slots=True)
class PerceptionResult:
    """Output produced by the CivicLens perception pipeline."""

    event: PerceptionEvent
    image: np.ndarray

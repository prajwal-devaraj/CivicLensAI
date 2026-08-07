from dataclasses import dataclass

from .detection import ObjectDetection


@dataclass(frozen=True, slots=True)
class VisionPrediction:
    """Structured output produced by a CivicLens vision model."""

    detections: tuple[ObjectDetection, ...]

    @property
    def count(self) -> int:
        return len(self.detections)

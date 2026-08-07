from dataclasses import dataclass

from .bounding_box import BoundingBox


@dataclass(frozen=True, slots=True)
class ObjectDetection:
    """A single object detected in a camera frame."""

    label: str
    confidence: float
    bounding_box: BoundingBox

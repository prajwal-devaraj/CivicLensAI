from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class BoundingBox:
    """Pixel-space bounding box for a detected object."""

    x_min: int
    y_min: int
    x_max: int
    y_max: int

    @property
    def width(self) -> int:
        return self.x_max - self.x_min

    @property
    def height(self) -> int:
        return self.y_max - self.y_min

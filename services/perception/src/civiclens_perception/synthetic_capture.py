import numpy as np

from .frame import CameraFrame


class SyntheticFrameCapture:
    """Deterministic camera source used for development and testing."""

    def __init__(
        self,
        source_id: str = "synthetic-camera",
        width: int = 1280,
        height: int = 720,
    ) -> None:
        self.source_id = source_id
        self.width = width
        self.height = height

    def capture(self) -> CameraFrame:
        image = np.zeros(
            (self.height, self.width, 3),
            dtype=np.uint8,
        )

        return CameraFrame(
            source_id=self.source_id,
            width=self.width,
            height=self.height,
            image=image,
        )

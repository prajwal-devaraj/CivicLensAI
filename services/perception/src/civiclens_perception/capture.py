from typing import Protocol

from .frame import CameraFrame


class FrameCapture(Protocol):
    """Contract for anything that can capture a camera frame."""

    def capture(self) -> CameraFrame:
        """Capture and return the next frame."""
        ...

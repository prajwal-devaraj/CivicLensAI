import cv2
import numpy as np

from .errors import FrameCaptureError
from .frame import CameraFrame


class VisionPreprocessor:
    """Prepare raw camera frames for downstream vision models."""

    def prepare(
        self,
        frame: CameraFrame,
        target_width: int = 640,
        target_height: int = 640,
    ) -> np.ndarray:
        if frame.image is None:
            raise FrameCaptureError("Camera frame does not contain image data")

        resized = cv2.resize(
            frame.image,
            (target_width, target_height),
        )

        return cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

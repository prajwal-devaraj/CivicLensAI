import cv2

from .errors import CameraUnavailableError, FrameCaptureError
from .frame import CameraFrame


class OpenCVCameraCapture:
    """Capture frames from a real camera using OpenCV."""

    def __init__(
        self,
        source_id: str = "front-camera",
        device_index: int = 0,
    ) -> None:
        self.source_id = source_id
        self.device_index = device_index
        self._capture = cv2.VideoCapture(device_index)

        if not self._capture.isOpened():
            raise CameraUnavailableError(
                f"Camera device {device_index} is unavailable"
            )

    def capture(self) -> CameraFrame:
        success, image = self._capture.read()

        if not success or image is None:
            raise FrameCaptureError(
                f"Failed to capture frame from device {self.device_index}"
            )

        height, width = image.shape[:2]

        return CameraFrame(
            source_id=self.source_id,
            width=width,
            height=height,
            image=image,
        )

    def close(self) -> None:
        self._capture.release()

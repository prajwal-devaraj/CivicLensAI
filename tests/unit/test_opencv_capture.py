from unittest.mock import MagicMock, patch

import numpy as np
from civiclens_perception.opencv_capture import OpenCVCameraCapture


@patch("civiclens_perception.opencv_capture.cv2.VideoCapture")
def test_opencv_capture_returns_camera_frame(mock_video_capture):
    mock_camera = MagicMock()
    mock_camera.isOpened.return_value = True
    mock_camera.read.return_value = (
        True,
        np.zeros((480, 640, 3), dtype=np.uint8),
    )
    mock_video_capture.return_value = mock_camera

    camera = OpenCVCameraCapture(
        source_id="front-camera",
        device_index=0,
    )

    frame = camera.capture()

    assert frame.source_id == "front-camera"
    assert frame.width == 640
    assert frame.height == 480
    assert frame.image is not None
    assert frame.image.shape == (480, 640, 3)

    camera.close()
    mock_camera.release.assert_called_once()

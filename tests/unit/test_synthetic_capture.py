from services.perception.src.civiclens_perception.synthetic_capture import (
    SyntheticFrameCapture,
)


def test_synthetic_capture_returns_camera_frame():
    capture = SyntheticFrameCapture(
        source_id="test-camera",
        width=640,
        height=480,
    )

    frame = capture.capture()

    assert frame.source_id == "test-camera"
    assert frame.width == 640
    assert frame.height == 480

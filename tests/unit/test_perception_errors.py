from civiclens_perception.errors import (
    CameraUnavailableError,
    FrameCaptureError,
    PerceptionError,
)


def test_camera_errors_inherit_from_perception_error():
    assert issubclass(CameraUnavailableError, PerceptionError)
    assert issubclass(FrameCaptureError, PerceptionError)

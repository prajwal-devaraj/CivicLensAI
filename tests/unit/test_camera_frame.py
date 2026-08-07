from services.perception.src.civiclens_perception.frame import CameraFrame


def test_camera_frame_has_unique_identity():
    first = CameraFrame(source_id="front-camera", width=1280, height=720)
    second = CameraFrame(source_id="front-camera", width=1280, height=720)

    assert first.frame_id != second.frame_id
    assert first.source_id == "front-camera"
    assert first.width == 1280
    assert first.height == 720
    assert first.captured_at <= second.captured_at

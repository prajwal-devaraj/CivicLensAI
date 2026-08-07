from services.perception.src.civiclens_perception.camera import CameraSource


def test_camera_source_description():
    camera = CameraSource(source_id="front-camera", device_index=0)

    assert camera.describe() == {
        "source_id": "front-camera",
        "device_index": 0,
        "modality": "vision",
    }

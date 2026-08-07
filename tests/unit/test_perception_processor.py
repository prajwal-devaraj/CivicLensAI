from services.perception.src.civiclens_perception.frame import CameraFrame
from services.perception.src.civiclens_perception.processor import PerceptionProcessor


def test_processor_converts_frame_into_event():
    frame = CameraFrame(source_id="front-camera", width=1280, height=720)
    processor = PerceptionProcessor()

    event = processor.process_frame(frame)

    assert event.source == "front-camera"
    assert event.modality == "vision"

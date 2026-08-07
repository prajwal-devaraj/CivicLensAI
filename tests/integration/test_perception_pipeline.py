from services.perception.src.civiclens_perception.pipeline import PerceptionPipeline
from services.perception.src.civiclens_perception.processor import PerceptionProcessor
from services.perception.src.civiclens_perception.synthetic_capture import SyntheticFrameCapture


def test_perception_pipeline_runs_end_to_end():
    capture = SyntheticFrameCapture(
        source_id="front-camera",
        width=640,
        height=480,
    )
    processor = PerceptionProcessor()
    pipeline = PerceptionPipeline(capture=capture, processor=processor)

    event = pipeline.run_once()

    assert event.source == "front-camera"
    assert event.modality == "vision"

from civiclens_perception.mock_vision_model import MockVisionModel
from civiclens_perception.pipeline import PerceptionPipeline
from civiclens_perception.preprocessing import VisionPreprocessor
from civiclens_perception.processor import PerceptionProcessor
from civiclens_perception.synthetic_capture import SyntheticFrameCapture


def test_perception_pipeline_runs_end_to_end():
    pipeline = PerceptionPipeline(
        capture=SyntheticFrameCapture(
            source_id="front-camera",
            width=640,
            height=480,
        ),
        processor=PerceptionProcessor(),
        preprocessor=VisionPreprocessor(),
        model=MockVisionModel(),
    )

    result = pipeline.run_once()

    assert result.event.source == "front-camera"
    assert result.event.modality == "vision"
    assert result.image.shape == (640, 640, 3)
    assert result.prediction.label == "synthetic-scene"
    assert result.prediction.confidence == 1.0

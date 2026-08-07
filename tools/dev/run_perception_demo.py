from civiclens_perception.pipeline import PerceptionPipeline
from civiclens_perception.preprocessing import VisionPreprocessor
from civiclens_perception.processor import PerceptionProcessor
from civiclens_perception.synthetic_capture import SyntheticFrameCapture


def main() -> None:
    pipeline = PerceptionPipeline(
        capture=SyntheticFrameCapture(
            source_id="civiclens-front-camera",
            width=1280,
            height=720,
        ),
        processor=PerceptionProcessor(),
        preprocessor=VisionPreprocessor(),
    )

    result = pipeline.run_once()
    event = result.event

    print("CivicLens AI — Perception Result")
    print(f"Event ID    : {event.event_id}")
    print(f"Source      : {event.source}")
    print(f"Modality    : {event.modality}")
    print(f"Time        : {event.timestamp.isoformat()}")
    print(f"Image shape : {result.image.shape}")


if __name__ == "__main__":
    main()

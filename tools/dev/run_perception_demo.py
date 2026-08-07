from civiclens_perception.pipeline import PerceptionPipeline
from civiclens_perception.processor import PerceptionProcessor
from civiclens_perception.synthetic_capture import SyntheticFrameCapture


def main() -> None:
    capture = SyntheticFrameCapture(
        source_id="civiclens-front-camera",
        width=1280,
        height=720,
    )

    pipeline = PerceptionPipeline(
        capture=capture,
        processor=PerceptionProcessor(),
    )

    event = pipeline.run_once()

    print("CivicLens AI — Perception Event")
    print(f"Event ID : {event.event_id}")
    print(f"Source   : {event.source}")
    print(f"Modality : {event.modality}")
    print(f"Time     : {event.timestamp.isoformat()}")


if __name__ == "__main__":
    main()

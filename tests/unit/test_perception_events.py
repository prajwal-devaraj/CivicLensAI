from services.perception.src.civiclens_perception.events import PerceptionEvent


def test_perception_events_have_unique_ids():
    first = PerceptionEvent(source="camera-1", modality="vision")
    second = PerceptionEvent(source="camera-1", modality="vision")

    assert first.event_id != second.event_id
    assert first.timestamp <= second.timestamp

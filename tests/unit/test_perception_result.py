import numpy as np
from civiclens_perception.events import PerceptionEvent
from civiclens_perception.result import PerceptionResult


def test_perception_result_holds_event_and_image():
    event = PerceptionEvent(
        source="front-camera",
        modality="vision",
    )
    image = np.zeros((320, 320, 3), dtype=np.uint8)

    result = PerceptionResult(
        event=event,
        image=image,
    )

    assert result.event == event
    assert result.image.shape == (320, 320, 3)

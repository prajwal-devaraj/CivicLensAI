from .events import PerceptionEvent
from .frame import CameraFrame


class PerceptionProcessor:
    """Transforms raw perception inputs into CivicLens events."""

    def process_frame(self, frame: CameraFrame) -> PerceptionEvent:
        return PerceptionEvent(
            source=frame.source_id,
            modality="vision",
        )

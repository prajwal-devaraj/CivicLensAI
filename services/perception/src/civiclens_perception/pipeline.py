from .capture import FrameCapture
from .events import PerceptionEvent
from .processor import PerceptionProcessor


class PerceptionPipeline:
    """Runs the CivicLens perception flow from capture to event."""

    def __init__(
        self,
        capture: FrameCapture,
        processor: PerceptionProcessor,
    ) -> None:
        self.capture = capture
        self.processor = processor

    def run_once(self) -> PerceptionEvent:
        frame = self.capture.capture()
        return self.processor.process_frame(frame)

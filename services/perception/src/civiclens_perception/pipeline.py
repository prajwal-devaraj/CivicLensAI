from .capture import FrameCapture
from .preprocessing import VisionPreprocessor
from .processor import PerceptionProcessor
from .result import PerceptionResult


class PerceptionPipeline:
    """Run capture, preprocessing, and perception as one pipeline."""

    def __init__(
        self,
        capture: FrameCapture,
        processor: PerceptionProcessor,
        preprocessor: VisionPreprocessor,
    ) -> None:
        self.capture = capture
        self.processor = processor
        self.preprocessor = preprocessor

    def run_once(self) -> PerceptionResult:
        frame = self.capture.capture()
        image = self.preprocessor.prepare(frame)
        event = self.processor.process_frame(frame)

        return PerceptionResult(
            event=event,
            image=image,
        )

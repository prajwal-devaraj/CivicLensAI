from .capture import FrameCapture
from .preprocessing import VisionPreprocessor
from .processor import PerceptionProcessor
from .result import PerceptionResult
from .vision_model import VisionModel


class PerceptionPipeline:
    """Run capture, preprocessing, inference, and perception."""

    def __init__(
        self,
        capture: FrameCapture,
        processor: PerceptionProcessor,
        preprocessor: VisionPreprocessor,
        model: VisionModel,
    ) -> None:
        self.capture = capture
        self.processor = processor
        self.preprocessor = preprocessor
        self.model = model

    def run_once(self) -> PerceptionResult:
        frame = self.capture.capture()
        image = self.preprocessor.prepare(frame)
        prediction = self.model.infer(image)
        event = self.processor.process_frame(frame)

        return PerceptionResult(
            event=event,
            image=image,
            prediction=prediction,
        )

from .prediction import VisionPrediction


class DetectionFilter:
    """Filter low-confidence vision detections."""

    def __init__(self, minimum_confidence: float = 0.5) -> None:
        if not 0.0 <= minimum_confidence <= 1.0:
            raise ValueError("minimum_confidence must be between 0.0 and 1.0")

        self.minimum_confidence = minimum_confidence

    def apply(self, prediction: VisionPrediction) -> VisionPrediction:
        detections = tuple(
            detection
            for detection in prediction.detections
            if detection.confidence >= self.minimum_confidence
        )

        return VisionPrediction(detections=detections)

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class VisionPrediction:
    """Structured output produced by a CivicLens vision model."""

    label: str
    confidence: float

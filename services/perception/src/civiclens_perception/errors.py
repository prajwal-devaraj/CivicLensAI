class PerceptionError(Exception):
    """Base error for CivicLens perception failures."""


class CameraUnavailableError(PerceptionError):
    """Raised when a camera device cannot be opened."""


class FrameCaptureError(PerceptionError):
    """Raised when a camera fails to capture a frame."""

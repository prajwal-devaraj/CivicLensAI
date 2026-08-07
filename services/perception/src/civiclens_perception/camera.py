from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CameraSource:
    source_id: str
    device_index: int = 0

    def describe(self) -> dict[str, str | int]:
        return {
            "source_id": self.source_id,
            "device_index": self.device_index,
            "modality": "vision",
        }

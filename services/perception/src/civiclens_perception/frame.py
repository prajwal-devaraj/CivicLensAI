from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class CameraFrame:
    source_id: str
    width: int
    height: int
    frame_id: UUID = field(default_factory=uuid4)
    captured_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

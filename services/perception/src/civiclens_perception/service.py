class PerceptionService:
    """Core entry point for CivicLens perception."""

    name = "civiclens-perception"

    def health(self) -> dict[str, str]:
        return {"service": self.name, "status": "healthy"}

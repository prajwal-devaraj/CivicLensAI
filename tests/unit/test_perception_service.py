from services.perception.src.civiclens_perception.service import PerceptionService


def test_perception_service_health():
    service = PerceptionService()

    assert service.health() == {
        "service": "civiclens-perception",
        "status": "healthy",
    }

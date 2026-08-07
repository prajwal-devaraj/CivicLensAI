from civiclens_perception.bounding_box import BoundingBox


def test_bounding_box_dimensions():
    box = BoundingBox(
        x_min=10,
        y_min=20,
        x_max=110,
        y_max=220,
    )

    assert box.width == 100
    assert box.height == 200

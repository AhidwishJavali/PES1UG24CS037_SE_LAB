import pytest

from customs_duty import clearance_channel, duty_rate, total_duty


@pytest.mark.parametrize(
    ("category", "origin", "expected"),
    [
        ("weapons", "FTA", None),
        ("electronics", "FTA", 0.10),
        ("electronics", "US", 0.20),
        ("clothing", "FTA", 0.05),
        ("clothing", "US", 0.12),
        ("books", "US", 0),
        ("furniture", "US", 0.15),
    ],
)
def test_duty_rate_all_decision_outcomes(category, origin, expected):
    if category in {"weapons", "narcotics"}:
        with pytest.raises(ValueError, match="prohibited item"):
            duty_rate(category, origin)
    else:
        assert duty_rate(category, origin) == expected


@pytest.mark.parametrize(
    ("category", "value", "origin", "is_gift", "expected"),
    [
        ("electronics", -1, "US", False, "error"),
        ("electronics", 5000, "US", True, 0),
        ("electronics", 6000, "US", True, 200),
        ("electronics", 1000, "US", False, 0),
        ("clothing", 5100, "FTA", True, 50),
        ("electronics", 2000, "US", False, 400),
        ("books", 2000, "US", False, 0),
    ],
)
def test_total_duty_all_decision_outcomes(category, value, origin, is_gift, expected):
    if expected == "error":
        with pytest.raises(ValueError, match="negative value"):
            total_duty(category, value, origin, is_gift)
    else:
        assert total_duty(category, value, origin, is_gift) == expected


@pytest.mark.parametrize(
    ("value", "category", "has_documents", "expected"),
    [
        (1000, "weapons", True, "refuse"),
        (100001, "books", True, "inspect"),
        (20000, "books", False, "green"),
        (25000, "books", False, "inspect"),
        (25000, "books", True, "green"),
    ],
)
def test_clearance_channel_all_decision_outcomes(value, category, has_documents, expected):
    assert clearance_channel(value, category, has_documents) == expected

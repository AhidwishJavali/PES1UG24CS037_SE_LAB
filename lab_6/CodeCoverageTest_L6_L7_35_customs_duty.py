import pytest

from customs_duty import clearance_channel, duty_rate, total_duty


@pytest.mark.parametrize(
    ("category", "origin", "expected"),
    [
        ("electronics", "FTA", 0.10),
        ("electronics", "US", 0.20),
        ("clothing", "FTA", 0.05),
        ("clothing", "US", 0.12),
        ("books", "US", 0),
        ("furniture", "US", 0.15),
    ],
)
def test_duty_rate_categories(category, origin, expected):
    assert duty_rate(category, origin) == expected


@pytest.mark.parametrize("category", ["weapons", "narcotics"])
def test_duty_rate_rejects_prohibited_items(category):
    with pytest.raises(ValueError, match="prohibited item"):
        duty_rate(category, "US")


def test_total_duty_rejects_negative_value():
    with pytest.raises(ValueError, match="negative value"):
        total_duty("electronics", -1, "US", False)


def test_gift_at_or_below_exemption_has_no_duty():
    assert total_duty("electronics", 5000, "US", True) == 0


def test_gift_above_exemption_is_charged_on_excess_value():
    assert total_duty("electronics", 6000, "US", True) == 200


def test_non_gift_at_or_below_threshold_has_no_duty():
    assert total_duty("electronics", 1000, "US", False) == 0


def test_small_positive_duty_uses_minimum_charge():
    assert total_duty("clothing", 5100, "FTA", True) == 50


def test_duty_at_least_minimum_is_not_adjusted():
    assert total_duty("electronics", 2000, "US", False) == 400


def test_duty_free_category_remains_free_above_threshold():
    assert total_duty("books", 2000, "US", False) == 0


@pytest.mark.parametrize(
    ("value", "category", "has_documents", "expected"),
    [
        (1000, "weapons", True, "refuse"),
        (100001, "books", True, "inspect"),
        (25000, "books", False, "inspect"),
        (25000, "books", True, "green"),
        (20000, "books", False, "green"),
    ],
)
def test_clearance_channel_outcomes(value, category, has_documents, expected):
    assert clearance_channel(value, category, has_documents) == expected

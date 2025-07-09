import datetime
from unittest.mock import patch, MagicMock
from pytest import mark

from app.main import outdated_products


@mark.parametrize(
    "products, today_date, expected",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600,
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160,
                },
            ],
            datetime.date(2022, 2, 5),
            ["duck"],
        ),
        (
            [
                {
                    "name": "today_product",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120,
                },
            ],
            datetime.date(2022, 2, 5),
            [],
        ),
        (
            [
                {
                    "name": "yesterday_product",
                    "expiration_date": datetime.date(2022, 2, 4),
                    "price": 100,
                },
            ],
            datetime.date(2022, 2, 5),
            ["yesterday_product"],
        ),
    ],
)
@patch("app.main.datetime.date")
def test_outdated_products(
    mock_date: MagicMock,
    products: list,
    today_date: datetime.date,
    expected: list,
) -> None:
    mock_date.today.return_value = today_date

    assert outdated_products(products) == expected

import unittest
import datetime

from app.main import outdated_products


class TestOutdatedProducts(unittest.TestCase):
    def test_deadline_expired(self) -> None:
        products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2024, 10, 10),
                "price": 600,
            }
        ]
        outdated_products(products)
        self.assertEqual(products[0]["name"], "salmon")

    def test_multiple_products(self) -> None:
        products = [
            {
                "name": "chicken",
                "expiration_date": datetime.date(2024, 10, 16),
                "price": 120
            },
            {
                "name": "salmon",
                "expiration_date": datetime.date(2024, 10, 10),
                "price": 600,
            }
        ]
        outdated_products(products)
        self.assertEqual(products[0]["name"], "salmon")

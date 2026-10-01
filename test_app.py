import pytest
from app import SalesAnalyzer, get_best_selling_product


def test_calculate_revenue():
    analyzer = SalesAnalyzer()

    result = analyzer.calculate_revenue(5, 10.0)

   assert result == 50.0


def test_negative_quantity_is_rejected():
    analyzer = SalesAnalyzer()

    with pytest.raises(ValueError):
        analyzer.calculate_revenue(-5, 10.0)


def test_best_selling_product():
    products = [
        {"name": "Laptop", "quantity": 10},
        {"name": "Phone", "quantity": 25},
        {"name": "Tablet", "quantity": 15}
    ]

    result = get_best_selling_product(products)

    assert result["name"] == "Phone"
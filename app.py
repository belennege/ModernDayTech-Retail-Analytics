class SalesAnalyzer:
    def calculate_revenue(self, quantity, unit_price):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        if unit_price < 0:
            raise ValueError("Unit price cannot be negative")

        return quantity * unit_price


def get_best_selling_product(products):
    if not products:
        return None

    return max(products, key=lambda product: product["quantity"])


if __name__ == "__main__":
    analyzer = SalesAnalyzer()

    revenue = analyzer.calculate_revenue(5, 10.0)

    print(f"Transaction revenue: £{revenue:.2f}")
import unittest


class Stock:
    """
    Our Stock class for keep stocks
    """

    def __init__(self, symbol):
        self.symbol = symbol
        self.price = None


class StockTest(unittest.TestCase):
    """
    Testing stocks
    """

    def test_price_of_a_new_stock_class_should_be_None(self):
        stock = Stock("GONG")
        self.assertIsNone(stock.price)


if __name__ == "__main__":
    unittest.main()

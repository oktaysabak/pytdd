import unittest
from ..stock import Stock
from datetime import datetime


class StockTest(unittest.TestCase):
    """
    Testing stocks
    """

    def test_price_of_a_new_stock_class_should_be_None(self):
        stock = Stock("GONG")
        self.assertIsNone(stock.price)

    def test_stock_update(self):
        """
        An update should set the price on the stock object
        We will be using the `datetime` module for the timestamp
        """
        stock = Stock("GONG")
        stock.update(datetime(2020, 12, 25), price=10)
        self.assertEqual(10, stock.price)

    def test_negative_price_should_throw_ValueEror(self):
        stock = Stock("GONG")
        with self.assertRaises(ValueError):
            stock.update(datetime(2020, 12, 25), -1)

    def test_stock_price_should_give_the_latest_price(self):
        stock = Stock("GONG")
        stock.update(datetime(2020, 12, 21), price=10)
        stock.update(datetime(2020, 12, 22), price=8.4)
        self.assertAlmostEqual(8.4, stock.price, delta=0.0001)
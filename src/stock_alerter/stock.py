class Stock:
    """
    Our Stock class for keep stocks
    """

    def __init__(self, symbol):
        self.symbol = symbol
        self.price = None

    def update(self, timestamp, price):
        """
        Update stock object price.
        """
        if price < 0:
            raise ValueError("price should not be negative")
        self.price = price

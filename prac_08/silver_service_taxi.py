"""
prac 08
SilverServiceTaxi Class
"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):

    price_per_km = 1.23
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness=0):
        super().__init__(name, fuel)
        self.fanciness = float(fanciness)
        self.price_per_km *= fanciness

    def get_fare(self):
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()} plus flagfall of {self.flagfall:.2f}"


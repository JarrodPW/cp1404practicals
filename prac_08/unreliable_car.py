"""
prac 08
UnreliableCar Class
"""
import random
from prac_08.car import Car


class UnreliableCar(Car):
    """Specialised version a care that include a reliability score out of 100"""

    def __init__(self, name, fuel, reliability=""):
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if random.randint(0, 100) < self.reliability:
            distance_driven = 0
        else:
            distance_driven = super().drive(distance)
        return distance_driven

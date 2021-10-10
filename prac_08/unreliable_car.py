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
            distance = 0
        else:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
        self.odometer += distance
        return distance

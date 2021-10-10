"""
Prac 08, UnreliableCar Class test
"""

from prac_08.unreliable_car import UnreliableCar

good_car = UnreliableCar("mostly good", 100, 90)
bad_car = UnreliableCar("dodgy", 100, 9)

for i in range(1, 11):
    print(f" Attempting to drive {i}km:")
    print(f"{good_car.name} drove {good_car.drive(i)}km.")
    print(f"{bad_car.name} drove {bad_car.drive(i)}km.")
print(good_car)
print(bad_car)

"""
Write lines of code for each of the following (hint: use the methods available in the Taxi class)
"""
from prac_08.taxi import Taxi

# 1.
new_taxi = Taxi("Prius 1", 100)

# 2.
new_taxi.drive(40)

# 3.
print(new_taxi)
print(new_taxi.get_fare())

# 4.
new_taxi.start_fare()
new_taxi.drive(100)

# 5.
print(new_taxi)
print(new_taxi.get_fare())

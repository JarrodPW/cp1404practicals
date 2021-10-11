"""
Prac 08, SilverServiceTaxi Class test
"""

from prac_08.silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("new_taxi", 100, 2)
taxi.drive(18)

print(taxi)
print(taxi.get_fare())

import random

# This code produces a random integer between 5 and 20, inclusive.
# The smallest possible integer is 5, and the largest possible is 20.
print(random.randint(5, 20))


# This code produces a random odd integer between 3 and 10 inclusive.
# The smallest possible integer is 3, and the largest possible is 9.
# The code could not produce a 4 as this number is outside the count.
print(random.randrange(3, 10, 2))  # 5, 9, 3, 5, 3


# This code produces a random float between 2.5 and 5.5, not-rounded and not inclusive.
# The smallest possible number you can produce is 2.5000000000000001, and the largest possible is 5.4999999999999999.
print(random.uniform(2.5, 5.5))

# Produce a random number between 1 and 100 inclusive
print(random.randint(1, 100))

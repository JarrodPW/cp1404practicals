"""
Practical 04 Warmup
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] will have the output 3
# numbers[-1] will have the output 2
# numbers[3] will have the output 1
# numbers[:-1] will have the output [3, 1, 4, 1, 5, 9]
# numbers[3:4] will have the output [1]
# 5 in numbers will have the output True
# 7 in numbers will have the output False
# "3" in numbers will have the output False
# numbers + [6, 5, 3] will have the output [3, 1, 4, 1, 5, 9, 6, 5, 3]

# # 1. Replace the first element of numbers with "ten"
numbers[0] = "ten"
print(numbers)

# # 2. Replace the last element on numbers with 1
numbers[-1] = 1
print(numbers)

# 3. Get all the elements from numbers except the first two
print(numbers[2:])

# 4. Check if 9 is an element of numbers
print(9 in numbers)

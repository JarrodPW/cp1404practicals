"""
Intermediate Exercises Prac 04
"""
# # 1. Basic list operations
# NUMBER_OF_NUMBERS = 5
#
#
# def main():
#     numbers = []
#     for i in range(NUMBER_OF_NUMBERS):
#         number = int(input("Number: "))
#         numbers.append(number)
#     print_interesting_statements(numbers)
#
#
# def print_interesting_statements(numbers):
#     print(f"The first number is {numbers[0]}")
#     print(f"The last number is {numbers[-1]}")
#     print(f"The smallest number is {min(numbers)}")
#     print(f"The largest number is {max(numbers)}")
#     print(f"The average of the number is {calculate_average(numbers)}")
#
#
# def calculate_average(numbers):
#     return sum(numbers) / len(numbers)
#
#
# main()
#
# # 2. Woefully inadequate security checker
# usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
#              'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
# username = input("Username: ")
# if username in usernames:
#     print("Access granted")
# else:
#     print("Access denied")

# 3. List Comprehensions
"""
CP1404/CP5632 Practical
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing",
              "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)

# list comprehension that creates a list containing the initials
# splits each name and adds the first letters of each part to a string
full_initials = [name.split()[0][0] + name.split()[1][0] for name in
                 full_names]
print(full_initials)

# one more example, using filtering to select only the names that start with A
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# use a list comprehension to create a list of all of the full_names
# in lowercase format
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
# use a list comprehension to create a list of integers
# from the above list of strings
numbers = [int(number) for number in almost_numbers]
print(numbers)

# use a list comprehension to create a list of only the numbers that are
# greater than 9 from the numbers (not strings) you just created
numbers_greater_than_nine = [number for number in numbers if number > 9]
print(numbers_greater_than_nine)

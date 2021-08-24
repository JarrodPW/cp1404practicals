"""
Intermediate Exercises Prac 04
"""
# 1. Basic list operations
NUMBER_OF_NUMBERS = 5


def main():
    numbers = []
    for i in range(NUMBER_OF_NUMBERS):
        number = int(input("Number: "))
        numbers.append(number)
    print_interesting_statements(numbers)


def print_interesting_statements(numbers):
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the number is {calculate_average(numbers)}")


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


main()

# 2. Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")

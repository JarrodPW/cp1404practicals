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

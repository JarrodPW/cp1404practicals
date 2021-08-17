"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50


def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)

# c
    generated_score = random.randint(0, 101)
    print(generated_score, determine_result(generated_score))


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASS_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


main()


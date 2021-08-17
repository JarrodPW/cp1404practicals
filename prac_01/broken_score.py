"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50
score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= EXCELLENT_THRESHOLD:
    print("Excellent")
elif score >= PASS_THRESHOLD:
    print("Passable")
else:
    print("Bad")


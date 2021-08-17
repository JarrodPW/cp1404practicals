"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
LOW_BONUS_PERCENTAGE = 0.1
HIGH_BONUS_PERCENTAGE = 0.15
BONUS_THRESHOLD = 1000

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= BONUS_THRESHOLD:
        bonus = sales * HIGH_BONUS_PERCENTAGE
    else:
        bonus = sales * LOW_BONUS_PERCENTAGE
    print(f"With a total sales amount of ${sales:.2f}, you will receive a ${bonus:.2f} bonus")
    sales = float(input("Enter sales: $"))
print("Have a nice day :)")

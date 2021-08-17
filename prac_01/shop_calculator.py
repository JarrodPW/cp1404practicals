"""
This program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied.
"""
DISCOUNT_RATE = 0.9         # Represents 10%
DISCOUNT_THRESHOLD = 100

total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item
if total_price > DISCOUNT_THRESHOLD:
    total_price *= DISCOUNT_RATE
print(f"Total price for {number_of_items} item/s is ${total_price:.2f}")

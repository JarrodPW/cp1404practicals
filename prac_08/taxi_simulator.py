"""
prac 08
Taxi simulator
"""
MENU = "Q)uit, C)hoose taxi, D)rive"

print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        pass
    elif choice == "D":
        pass
    else:
        print("Invalid menu option")
    print(MENU)
    choice = input(">>> ").upper()

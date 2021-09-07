"""
Write a program that uses the Guitar class
and uses a list to store all the user's guitars (keep inputting until they enter a blank name),
then print their details.
"""
from prac_06.guitar import Guitar

my_guitars = []

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    my_guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost:,.2f} added")
    name = input("Name: ")
print("These are my guitars:")
for i, guitar in enumerate(my_guitars, 1):
    vintage_status = ""
    if guitar.is_vintage():
        vintage_status = "(vintage)"
    print(f"Guitar {i}: {guitar.name} ({guitar.year}), worth ${guitar.cost:,.2f} {vintage_status}")

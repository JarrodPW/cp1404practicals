"""
Write a program that stores users' emails (unique keys) and names (values) in a dictionary.
"""

email_to_name = {}

email = input("Email: ")
while email != "":
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    print(f"Is your name {name}? (Y/n)", end ="")
    choice = input("").lower()
    if choice == "n":
        name = input("Name: ")
    email = input("Email: ")
for 

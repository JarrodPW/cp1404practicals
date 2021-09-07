"""
Write a program that stores users' emails (unique keys) and names (values) in a dictionary.
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        answer = input(f"Is your name {name}? (Y/n) ").lower()
        if answer != "y" and answer != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print("")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    return name


main()

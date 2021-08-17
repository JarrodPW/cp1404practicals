"""
Password Check Program
"""


def main():
    minimum_length = int(input("Minimum length: "))
    password = get_password(minimum_length)
    print_asterisks(password)


def print_asterisks(password):
    for i in range(len(password)):
        print("*", end="")


def get_password(minimum_length):
    password = input("Password: ")
    while len(password) < minimum_length:
        print("Invalid")
        password = input("Password: ")
    return password


main()

minimum_length = int(input("Minimum length: "))
password = input("Password: ")
while len(password) < minimum_length:
    print("Invalid")
    password = input("Password: ")
for i in range(len(password)):
    print("*", end="")

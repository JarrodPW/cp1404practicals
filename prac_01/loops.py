# 3. Display all of the odd numbers between 1 and 20 with a space between each one
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a) Display a count from 0 to 100 in 10s with a space between each one
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b) Display a count down from 20 to 1 with a space between each one
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c) Get a number from the user then print that amount of stars
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*", end="")
print()

# d) Get a number from the user then print that amount of lines with increasing stars
number_of_stars = int(input("Number of stars: "))
# Note: the for loop has an in-built counter
for i in range(1, number_of_stars + 1):
    print("*" * i)
print()

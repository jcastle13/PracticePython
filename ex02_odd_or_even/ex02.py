
print("Enter a number")
number = int(input("Number: "))


if (number % 4) == 0:
    print("The number", number, "is a multiple of 4.")
elif number % 2:
    print("The number", number, "is odd.")
else:
    print("The number", number, "is even.")

print("Now for something completely different")
print("Enter two numbers to divide.")
check = int(input("Enter a numerator: "))
num = int(input("Enter a denominator: "))

if (check % num) == 0:
    print("The numbers:", check, "&", num, "divides evenly.")
else:
    print("The numbers do not divide evenly.")

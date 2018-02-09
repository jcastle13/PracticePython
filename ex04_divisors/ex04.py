
print("Program to list all the divisors from a givin number.")

number = int(input("Input a number: "))

ans_list = []

for i in range(1,number+1):
    if (number % i) == 0:
        ans_list.append(i)


print("The list of divisors for", number, "is:", ans_list)

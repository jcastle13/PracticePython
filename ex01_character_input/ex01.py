
print("Hello and welcome")
print("Please enter your name")
name = input("name: ")

print("Please enter your age")
age = input("age: ")

print("How many times do you want to display the message?")
display = input("display: ")

years_old = 100 - int(age)
years_old = 2018 + years_old

for i in range(int(display)):
    print("You will be 100 years old in:", years_old)



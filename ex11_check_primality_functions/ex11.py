
print("A primality function that gets a number from the user and detects whether the number is prime or not.")

def check_prime(num):
    if num == 1 or num == 2:
        return True

    for i in range(2,num):
        if num % i == 0:
            return False

    return True


number = int(input("Enter the number to check if its a prime value: "))
print(check_prime(number))


'''
Below is a mini testbench to test out the function
'''
'''
ans_list = []
for i in range(1,1000):
    ## Test out the first 1000 numbers
    print("value:", i , ":", check_prime(i))
    if check_prime(i):
        ans_list.append(i)

print("prime numbers:", ans_list)
'''


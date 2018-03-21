

def fib_num(num):
    num = int(num)
    print("Generating {} fibonacci numbers.".format(num))
    result = []
    if num == 1:
        print("1")
        return
    elif num == 2:
        print("1 1")
        return
    else:
        result.append(1)
        result.append(1)

    prev = 1
    curr = 1
    for i in range(1,num):
        temp = prev + curr
        result.append(temp)
        #print("temp:", temp)
        prev = curr
        curr = temp

    print("result:", result)



print("Program to generate Fibonacci numbers.")
number = input("How many fibonacci numbers do you want to generate: ")

fib_num(number)


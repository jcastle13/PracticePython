
print("Reverse word order")

def rev_word_order(string):
    print("orig string:", string)
    temp = string.split(" ")
    result = []

    temp_count = len(temp) - 1
    for i in range(0, len(temp)):
        #print(temp[temp_count])
        result.append(temp[temp_count])
        temp_count -= 1

    print(" ".join(result))



string = input("Input string to reverse word order: ")

rev_word_order(string)


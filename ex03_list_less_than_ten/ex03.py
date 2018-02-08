
print("Retrieving all values on a list that are less than 5")

example_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

print("exmaple_list:", example_list)

#for i in example_list:
#    if i < 5:
#        print("i:", i)
#        new_list.append(i)
#print("new list:", new_list)

new_list = list(filter(lambda x: (x < 5), example_list))

print("new_list using lambda & filter:", new_list)

print("Enter a number for a list of numbers less than the value given.")
min_value = int(input("Enter number for new list: "))

new_list = list(filter(lambda x: (x < min_value), example_list))

print("user devfined new list:", new_list)


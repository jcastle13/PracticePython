print("Excercise 12: List Ends")

a = [5, 10, 15, 20, 25]

def new_list(a):
    print("original list:", a)
    result = []
    result.append(a[0])
    result.append(a[-1])
    print("new list:", result)
    

new_list(a)


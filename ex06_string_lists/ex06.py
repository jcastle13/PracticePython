print("Plindrome checker")

word = input("Type in a word to check if it's a palindrome: ")

length = len(word)
back = -1

for i in range(int(length/2)):
    if word[i] == word[back]:
        back = back - 1
    else:
        print("The word:", word, "is not a palindrome")
        exit()

# If the for loop ends that means we've hit a palindrome
print("The word:", word, "is a palindrome!!!")

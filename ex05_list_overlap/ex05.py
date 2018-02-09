
def compare_lists(a, b):
    print("List a:", a)
    print("List b:", b)

    # Below is the one liner :)
    ans = list(set(a) & set(b))

    return ans


def main():
    a = [5, 5, 13, 6, 3, 4, 5]
    b = [3, 4, 5, 93, 2, 3, 4, 5, 2]
    results = compare_lists(a, b)
    print("results:", results)



if __name__ == "__main__":
    main()

from collections import Counter

string = input("Please enter a string")
def most_frequent(string):
    test_str = string
    res = Counter(test_str)
    print("" + str(res))

most_frequent(string)

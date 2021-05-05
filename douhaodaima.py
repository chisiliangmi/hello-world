import os

def string(spam):
    string = ""
    for i in range(len(spam)-1):
        string += (str(spam[i]) + ", ")

    string += "and " + str(spam[-1])
    return string

if __name__ == "__main__":
    spam = ['apple', 'bananas', 'tofu', 'cats']
    print(string(spam))

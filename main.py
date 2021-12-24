# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def makeAnagram(a, b):
    arrayA = list(a)
    arrayB = list(b)

    x=0
    while x < len(arrayA):
        for y in range(len(arrayB)):
            if arrayA[x] == arrayB[y]:
                arrayA.pop(x)
                arrayB.pop(y)
                x = -1
                break
        x += 1
    return len(arrayA) + len(arrayB)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    a = input()

    b = input()

    print(makeAnagram(a,b))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

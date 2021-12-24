#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    if len(s) % 2 == 0:
        mid = int(len(s) / 2)
        arrayA = list(s[0:mid])
        arrayB = list(s[mid:len(s)])
        x = 0
        while x < len(arrayA):
            for y in range(len(arrayB)):
                if arrayA[x] == arrayB[y]:
                    arrayB.pop(y)
                    break
            x += 1
        return len(arrayB)

    else: return -1



    # Write your code here

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        print(anagram(s))



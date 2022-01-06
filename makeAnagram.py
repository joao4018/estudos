#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    arr = list(a.lower())
    arr2 = list(b.lower())
    x = 0
    while x < len(arr2):
        for y in range(len(arr)):
            if arr2[x] == arr[y]:
                arr2.pop(x)
                arr.pop(y)
                x = -1
                break
        x +=1

    return print(len(arr) + len(arr2))


if _name_ == '_main_':

    a = input()

    b = input()

    res = makeAnagram(a, b)
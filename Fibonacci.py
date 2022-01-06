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

def fibonacci(a):
    arr = [0,1]
    if a == 1:
        return 0
    elif a == 2:
        return 1
    else:
        for y in range(a-2):
           arr.append(arr[y+1] + arr[y])

    return arr[a-1]






if _name_ == '_main_':

    print(fibonacci(60))
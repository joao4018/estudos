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

def inverter(b):
    x = 0
    y = len(b) - 1
    while x < y:
        tmp  = b[y]
        b[y] = b[x]
        b[x] = tmp
        x += 1
        y -= 1

    return print(b)


if __name__ == '__main__':

    makeAnagram([1,2,3,2,2,2,1,1,1,3,2,1])
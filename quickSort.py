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

def quickSort(a):
    arrLeft = []
    arrRight = []
    if len(a) < 1:
        return a
    else:
        pivo = a.pop()

        for items in a:
            if items < pivo:
                arrLeft.append(items)
            else:
                arrRight.append(items)

    return quickSort(arrLeft) + [pivo] + quickSort(arrRight)





if _name_ == '_main_':

    print(quickSort([1,3,4,5,2,6,7,8,3,4,32,121,45,76,7567,567,567,56,73,41,1,23,2,4,6,76,5,674,6,34]))
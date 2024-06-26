#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = 0 
    neg = 0
    zero = 0
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        elif num == 0:
            zero += 1
        else:
            pass
    
    total = len(arr)
    pos_frac = (pos / total)
    neg_frac = neg / total
    zero_frac = zero / total

    print(f"{pos_frac:.6f}")
    print(f"{neg_frac:.6f}")
    print(f"{zero_frac:.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

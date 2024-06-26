#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    print(arr)
    min_sum = sum(arr[:-1])
    max_sum = sum(arr[1:])
    print(min_sum, max_sum)
    

if __name__ == '__main__':

    arr = [2,5,8,4,9]

    miniMaxSum(arr)

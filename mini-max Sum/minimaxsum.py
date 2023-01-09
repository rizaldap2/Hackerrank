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
        
    # sort the array
    arr.sort()
    
    # get the sum of the array
    sum = 0
    for i in range (len(arr)):
        sum += arr[i]
    
    # print the min and max
    print(sum - arr[len(arr)-1], end=" ")
    print(sum - arr[0])

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
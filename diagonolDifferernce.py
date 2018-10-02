#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    rl_diagonol = 0
    lr_diagonol = 0
    for i in range(0,n):
                lr_diagonol += arr[i][i]
                rl_diagonol += arr[i][n-i-1]
    test_diff = abs(lr_diagonol - rl_diagonol)
    return test_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

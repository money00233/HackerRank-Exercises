#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    length = len(arr)
    p_count = 0
    n_count = 0
    z_count = 0
    p_prob = 0.00000
    n_prob = 0.00000
    z_prob = 0.00000
    for i in range(len(arr)):
        if(arr[i] > 0):
            p_count += 1
        if(arr[i] == 0):
            z_count += 1
        if(arr[i] < 0):
            n_count += 1
    p_prob = p_count/length
    n_prob = n_count/length
    z_prob = z_count/length
    print(p_prob)
    print(n_prob)
    print(z_prob)
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

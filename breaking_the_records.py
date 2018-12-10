#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    high_break = 0
    low_break = 0
    max_score = scores[0]
    min_score = scores[0]
    for i in range(len(scores)):
        if(scores[i] > max_score):
            high_break += 1
            max_score = scores[i]
        if(scores[i] < min_score):
            low_break += 1
            min_score = scores[i]
    return high_break, low_break

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

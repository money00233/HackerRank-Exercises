#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    b_actual = 0
    split_ = 0
    #exclude_ = bill[1]
    b = int(b)
    for i in range(n):
        if(i != k):
            split_ += bill[i]
    b_actual = int(split_/2)
    if(b != b_actual):
        print(b - b_actual)
    else:
        print("Bon Appetit")
        
if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

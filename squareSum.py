#!/bin/python3
import math as mt
import sys
def squareSum(n):
    Sum_s = 0
    Sum = 0
    Sum_sq = 0
    for i in range(0,n+1):
        Sum_s += i*i
    for i in range(0,n+1):
        Sum += i
    Sum_sq = Sum*Sum
    diff = Sum_sq - Sum_s
    print(diff)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    squareSum(n)
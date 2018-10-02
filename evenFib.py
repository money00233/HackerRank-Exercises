#!/bin/python3

import sys
#!/bin/python3

def genFib(n):
    if n <= 1:
        return n
    else:
        return (genFib(n-1) + genFib(n-2))
def getFib(n):
    fib = []
    for i in range(0,n):
        fib.append(genFib(n))
        fib.reverse()
        n -= 1
    return fib
def getSum(n):
    Sum_ = 0
    test = getFib(n)
    for i in range(len(test)):
        if(test[i]%2 == 0):
            Sum_ += test[i]
    print(Sum_)
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    getSum(n)
    

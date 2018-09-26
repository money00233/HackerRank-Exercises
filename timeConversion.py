# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 01:26:40 2018

@author: Mani
"""

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    s1 = (s[:-2])
    p = ""
    s2 = s[-2:]
    if (s2 == 'AM'):
        if(s[:2] == '12'):
            p = str('00' + s[2:8])
        else:
            p = s[:-2]
    elif(s2 == 'PM'):
        if(s[:2] == '12'):
            p = s[:-2]
        else:
            p = str(int(s[:2]) + 12 ) + s[2:8]
    return p

        
    #
    # Write your code here.
    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

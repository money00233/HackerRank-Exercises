# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 01:25:49 2018

@author: Mani
"""

#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    grade = grades
    for i in range(len(grades)):
        if(grades[i] >= 40):
            if((grades[i] + (5 - grades[i]%5))%5 == 0):
              if((5 - grades[i]%5) < 3):
                grade[i] = grades[i] + (5 - grades[i]%5)
        if(grades[i]>=38 and grades[i]<40):
            if((grades[i] + (5 - grades[i]%5))%5 == 0):
                if((5 - grades[i]%5) < 3):
                    grade[i] = grades[i] + (5 - grades[i]%5)
    return grade
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()

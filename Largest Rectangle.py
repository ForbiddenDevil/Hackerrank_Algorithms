#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.

def largestRectangle(h):
    max_area = 0
    for i in range(len(h)):
        cnt = 0
        for j in range(i, -1, -1):
            if h[j] >= h[i]:
                cnt += 1
            else:
                break
        for k in range(i+1, len(h)):
            if h[k] >= h[i]:
                cnt += 1
            else:
                break
        area = h[i] * cnt
        if area > max_area:
            max_area = area
    return(max_area)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))
    # print(largest([-1, 0, 1, 2, 3]))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()


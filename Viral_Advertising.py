# Problem statement:
# https://www.hackerrank.com/challenges/strange-advertising/problem

import math
import os
import random
import re
import sys

def viralAdvertising(n):
    likes_n = 0
    people_received = 5
    for day in range(n):
        daily_likes = people_received // 2
        likes_n += daily_likes
        people_received = daily_likes * 3
        
    return likes_n
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
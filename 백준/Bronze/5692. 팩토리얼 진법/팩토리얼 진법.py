import sys
input = sys.stdin.readline
import math

while True:
    arr = list(input().rstrip())[::-1]
    if arr == ['0']:
        break
    
    sum_ = 0
    for i in range(len(arr)):
        sum_ += int(arr[i]) * math.factorial(i+1)
    
    print(sum_)
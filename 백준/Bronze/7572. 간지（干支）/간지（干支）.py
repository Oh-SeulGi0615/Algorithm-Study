import sys
input = sys.stdin.readline

from collections import deque

arr_10 = deque([i for i in range(10)])
arr_12 = deque([chr(i) for i in range(65, 77)])

arr_10.rotate(1)
arr_12.rotate(-5)

n = int(input())

arr_10.rotate(2013-n)
arr_12.rotate(2013-n)

print(arr_12[0] + str(arr_10[0]))
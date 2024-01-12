import sys
input = sys.stdin.readline

from math import gcd

n = int(input())
arr = list(map(int, input().split()))

if n == 2:
    gcd_n = gcd(arr[0],arr[1])
else:
    gcd_n = gcd(gcd(arr[0],arr[1]), arr[2])
    
for i in range(1, gcd_n+1):
        if gcd_n % i == 0:
            print(i)
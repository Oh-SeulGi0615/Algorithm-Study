import sys
input = sys.stdin.readline

n = int(input())
result = bin(n)[2:]
print(result)
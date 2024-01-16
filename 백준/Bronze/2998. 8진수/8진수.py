import sys
input = sys.stdin.readline

num = oct(int(input().rstrip(), 2))

print(num[2:])
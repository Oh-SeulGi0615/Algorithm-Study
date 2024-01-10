import sys
input = sys.stdin.readline

arr = [i**5 for i in list(map(int, list(input().rstrip())))]

print(sum(arr))
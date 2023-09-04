import sys
input = sys.stdin.readline

l, r, a = map(int, input().split())

arr = [min(l+i, r+(a-i)) * 2 for i in range(a+1)]
print(max(arr))
import sys
input = sys.stdin.readline

n = int(input())
round1 = sum(list(map(lambda x: abs(x), list(map(int, input().split())))))
round2 = sum(list(map(lambda x: -1 * abs(x), list(map(int, input().split())))))

print(round1 - round2)
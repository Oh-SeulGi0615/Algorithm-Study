import sys
input = sys.stdin.readline

string = input().split('(^0^)')
result = [i.count('@') for i in string]

print(*result)
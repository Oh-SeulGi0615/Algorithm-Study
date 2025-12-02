import sys
input = sys.stdin.readline

x, y = map(int, input().split())
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

total = sum(days[1:x]) + y
result = date[total % 7]

print(result)
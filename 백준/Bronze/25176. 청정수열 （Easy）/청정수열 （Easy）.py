import sys
input = sys.stdin.readline

a = int(input())

answer = 1
for i in range(1,a+1):
    answer = answer * i

print(answer)
import sys
input = sys.stdin.readline

n = int(input())
string = input().rstrip()

score = 0
for i in string:
    score += ord(i) - 64

print(score)
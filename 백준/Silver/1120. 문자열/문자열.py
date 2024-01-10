import sys
input = sys.stdin.readline

str1, str2 = input().split()

diff = 50
for i in range(len(str2) - len(str1) + 1):
    cnt = 0
    for a, b in zip(str1, str2[i:i+len(str1)]):
        if a != b:
            cnt += 1
    if cnt < diff:
        diff = cnt

print(diff)
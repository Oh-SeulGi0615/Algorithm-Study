import sys
input = sys.stdin.readline

N = int(input())

arr = []
for x in range(N):
    a = input().rstrip()
    arr.append([len(a), a])
arr.sort()

answer = []
for i in arr:
    answer.append(i[1])

for j in range(1,len(answer)):
    if answer[j-1] == answer[j]:
        pass
    else:
        print(answer[j-1])
print(answer[-1])
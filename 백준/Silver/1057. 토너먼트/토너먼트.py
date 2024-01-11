import sys
input = sys.stdin.readline

n, kim, lim = map(int, input().split())
arr = [i for i in range(1, n+1)]

cnt = 1
answer = []
while True:
    result = [arr[i*(2**cnt) : (i+1)*(2**cnt)] for i in range((len(arr) + (2**cnt) - 1) // (2**cnt))]

    for l in range(len(result)):
        if kim in result[l] and lim in result[l]:
            answer.append(cnt)

    if len(result[0]) == len(arr) or len(answer) > 0:
        break
    cnt += 1
    
print(answer[0])
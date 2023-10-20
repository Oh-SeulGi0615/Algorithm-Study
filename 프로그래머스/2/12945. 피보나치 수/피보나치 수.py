f = {0:0, 1:1}
for i in range(2, 100001):
    f[i] = f[i-1] + f[i-2]

def solution(n):
    answer = f[n] % 1234567
    return answer
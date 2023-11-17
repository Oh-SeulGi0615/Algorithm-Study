import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

dict_ = {i:0 for i in range(1, n+1)}
dict_[m] = 3

if k == dict_[m]:
    print(m)
elif k > dict_[m]:
    now = m
    while True:
        if dict_[now] == k:
            print(now)
            break
        if now < n:
            now += 1
            dict_[now] = dict_[now - 1] + 1
        else:
            now = 1
            dict_[now] = dict_[n] + 1

elif k < dict_[m]:
    now = m
    while True:
        if dict_[now] == k:
            print(now)
            break
        if now > 1:
            now -= 1
            dict_[now] = dict_[now + 1] - 1
        else:
            now = n
            dict_[now] = dict_[1] - 1
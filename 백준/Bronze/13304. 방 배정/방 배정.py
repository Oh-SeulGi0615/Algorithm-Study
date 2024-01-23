import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dict_ = {i:[] for i in range(1, 4)}

for _ in range(n):
    s, y = map(int, input().split())

    if y == 1 or y == 2:
        dict_[1].append(s)
    elif y == 3 or y == 4:
        dict_[2].append(s)
    else:
        dict_[3].append(s)

room = 0
for j in range(1, 4):
    if j == 1:
        if len(dict_[j]) % k == 0:
            room += len(dict_[j]) // k
        else:
            room += len(dict_[j]) // k + 1
    else:
        w, m = dict_[j].count(0), dict_[j].count(1)
        if w % k == 0:
            room += w // k
        else:
            room += w // k + 1

        if m % k == 0:
            room += m // k
        else:
            room += m // k + 1

print(room)
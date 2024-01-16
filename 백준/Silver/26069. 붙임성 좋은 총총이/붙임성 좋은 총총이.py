import sys
input = sys.stdin.readline

list_ = {}
for _ in range(int(input())):
    a, b = map(str, input().split())
    
    if a not in list_:
        list_[a] = 0
    if b not in list_:
        list_[b] = 0

    if a == 'ChongChong' or b == 'ChongChong' or list_[a] == 1 or list_[b] == 1:
        list_[a], list_[b] = 1, 1

cnt = list(list_.values()).count(1)
print(cnt)
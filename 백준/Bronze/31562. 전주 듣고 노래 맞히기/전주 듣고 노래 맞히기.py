n, m = map(int, input().split())

dict_ = {}
for _ in range(n):
    arr = list(input().split())
    dict_[arr[1]] = arr[2:5]

for _ in range(m):
    arr2 = list(input().split())

    if arr2 not in dict_.values():
        print('!')
    elif list(dict_.values()).count(arr2) >= 2:
        print('?')
    else:
        for k, v in dict_.items():
            if arr2 == v:
                print(k)
                break
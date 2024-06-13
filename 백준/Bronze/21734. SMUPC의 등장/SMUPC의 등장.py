list_ = list(input().rstrip())

for i in list_:
    arr = list(map(int, str(ord(i))))
    print(i * sum(arr))
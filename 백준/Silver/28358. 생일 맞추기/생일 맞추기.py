import sys
input = sys.stdin.readline

month = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    day = [str(i) for i in range(10) if arr[i] == 1]

    cnt = 0
    day_str = {str(i) + ' ' + str(j) : 0 for i in range(1, 13) for j in range(1, month[i]+1)}

    for i in day_str.keys():
        for j in day:
            if j in i:
                day_str[i] = 1

    print(list(day_str.values()).count(0))
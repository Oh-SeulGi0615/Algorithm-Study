import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = list(map(int, input().split()))

    stat = arr[:4]
    equip = arr[4:]

    stat2 = []
    for i in range(4):
        stat2.append(stat[i] + equip[i])

    if stat2[0] < 1:
        stat2[0] = 1
    if stat2[1] < 1:
        stat2[1] = 1
    if stat2[2] < 0:
        stat2[2] = 0

    power = stat2[0] + stat2[1] * 5 + stat2[2] * 2 + stat2[3] * 2
    print(power)
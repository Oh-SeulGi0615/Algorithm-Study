import sys
input = sys.stdin.readline

r, b = map(int, input().split())

hv = int((r - 4) / 2)
hv_list = [[i, hv-i] for i in range(1, hv)]

for num in hv_list:
    if num[0] * num[1] == b:
        print(max(num)+2, min(num)+2)
        break
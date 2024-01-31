import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = list(map(int, input().split(':')))
    bin_arr = [str(bin(i))[2:].zfill(6) for i in arr]

    result_v = ''
    result_h = ''.join(bin_arr)

    for i in range(6):
        for j in bin_arr:
            result_v += j[i]

    print(result_v, result_h)
import sys
input = sys.stdin.readline

from itertools import product

n = int(input())
m = int(input())

if m == 0:
    if n == 100:
        print(0)
    else:
        print(min(len(str(n)), abs(100-n)))
elif m == 10:
    arr = list(map(int, input().split()))
    print(abs(100-n))
else:
    arr = list(map(int, input().split()))
    button = [i for i in range(10) if i not in arr]
    
    channel = []
    for i in range(1, len(str(n))+2):
        num_list = [int(''.join(map(str, j))) for j in product(button, repeat=i)]
        channel.extend(num_list)

    channel = sorted(channel, key=lambda x: abs(x - n))
    result = len(str(channel[0])) + abs(channel[0] - n)
    print(min(result, abs(100-n)))
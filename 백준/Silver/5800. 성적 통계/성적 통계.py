import sys
input = sys.stdin.readline

for i in range(1, int(input())+1):
    arr = list(map(int, input().split()))[1:]
    arr2 = sorted(arr, key=lambda x: -x)
    
    largest_gap = 0
    for j in range(1, len(arr2)):
        if abs(arr2[j] - arr2[j-1]) > largest_gap:
            largest_gap = abs(arr2[j] - arr2[j-1])

    print(f'Class {i}')
    print(f'Max {max(arr)}, Min {min(arr)}, Largest gap {largest_gap}')
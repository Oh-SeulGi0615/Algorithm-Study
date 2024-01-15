import sys
input = sys.stdin.readline

arr = [i for i in range(1, int(input())+1)]

if len(arr) == 1:
    print(arr[0])
else:
    arr1 = arr
    while True:
        arr2 = []
        for i in range(len(arr1)):
            if i % 2 == 1:    
                arr2.append(arr1[i])
        
        if len(arr2) == 1:
            break
        
        arr1 = arr2

    print(arr2[0])
import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr2 = list(map(int, input().split()))
    arr.extend(arr2)

white, blue = 0, 0

def divide(arr, n):
    global white, blue

    if 0 in arr and 1 not in arr:
        white += 1
    elif 0 not in arr and 1 in arr:
        blue += 1
    elif 0 in arr and 1 in arr:
        arr_ = [arr[i * n:(i + 1) * n] for i in range(int(len(arr)/n))]
        arr2, arr3, arr4, arr5 = [], [], [], []

        for i in range(len(arr_)):
            for j in range(len(arr_)):
                if i < int(len(arr_) / 2):
                    if j < int(len(arr_) / 2):
                        arr2.append(arr_[i][j])
                    else:
                        arr3.append(arr_[i][j])
                else:
                    if j < int(len(arr_) / 2):
                        arr4.append(arr_[i][j])
                    else:
                        arr5.append(arr_[i][j])
        
        if n > 1:
            for k in [arr2, arr3, arr4, arr5]:
                divide(k, int(n / 2))

divide(arr, n)
print(white, blue, sep='\n')
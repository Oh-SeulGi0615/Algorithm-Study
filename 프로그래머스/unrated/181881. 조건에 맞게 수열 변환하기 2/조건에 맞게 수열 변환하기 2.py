def solution(arr):
    x = 0
    while True:
        arr2 = []

        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr2.append(int(arr[i] / 2))
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr2.append(arr[i] * 2 + 1)
            else:
                arr2.append(arr[i])

        if arr == arr2:
            return x
            break
        arr = arr2
        x += 1
            
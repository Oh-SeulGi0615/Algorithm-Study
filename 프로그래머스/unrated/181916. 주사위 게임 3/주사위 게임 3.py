def solution(a, b, c, d):
    arr = [a, b, c, d]
    arr.sort()
    
    arr2 = list(set(arr))
    if len(arr2) == 1:
        return 1111 * arr2[0]
    elif len(arr2) == 2:
        if arr[0] == arr[1] == arr[2]:
            return (10 * arr[0] + arr[-1]) ** 2
        elif arr[1] == arr[2] == arr[-1]:
            return (10 * arr[1] + arr[0]) ** 2
        elif arr[0] == arr[1] and arr[2] == arr[-1]:
            return (arr[0] + arr[2]) * abs(arr[0] - arr[2])
    elif len(arr2) == 3:
        if arr[0] == arr[1]:
            return arr[2] * arr[3]
        elif arr[1] == arr[2]:
            return arr[0] * arr[3]
        elif arr[2] == arr[3]:
            return arr[0] * arr[1]
    elif len(arr2) == 4:
        return min(arr)
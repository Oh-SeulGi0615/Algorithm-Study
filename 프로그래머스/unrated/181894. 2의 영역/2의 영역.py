def solution(arr):
    if 2 not in arr:
        return [-1]
    else:
        arr2 = []
        for i in range(len(arr)):
            if arr[i] == 2:
                arr2.append(i)
        if len(arr2) == 1:
            return [arr[arr2[0]]]
        else:
            return arr[arr2[0] : arr2[-1]+1]
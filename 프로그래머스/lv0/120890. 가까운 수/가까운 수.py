def solution(array, n):
    array.sort()
    distance = [abs(n-i) for i in array]
    return array[distance.index(min(distance))]
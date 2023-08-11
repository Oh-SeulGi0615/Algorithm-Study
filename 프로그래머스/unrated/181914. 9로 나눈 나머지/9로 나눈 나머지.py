def solution(number):
    arr = list(map(int, list(str(number))))
    return sum(arr) % 9
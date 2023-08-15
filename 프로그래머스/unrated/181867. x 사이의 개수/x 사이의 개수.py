def solution(myString):
    arr = myString.split('x')
    answer = [len(i) for i in arr]
    return answer
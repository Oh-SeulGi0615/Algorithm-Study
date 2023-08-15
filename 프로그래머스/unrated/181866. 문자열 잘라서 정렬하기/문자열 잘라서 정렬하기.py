def solution(myString):
    myString = myString.split('x')
    answer = [i for i in myString if i != '']
    answer.sort()
    return answer
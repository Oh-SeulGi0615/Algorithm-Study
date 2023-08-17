def solution(myString):
    answer = ['l' if ord(i) < ord('l') else i for i in myString]
    return ''.join(answer)
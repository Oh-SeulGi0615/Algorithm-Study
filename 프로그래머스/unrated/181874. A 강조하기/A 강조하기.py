def solution(myString):
    answer = [myString[i].upper() if myString[i] == 'a' else 'A' if myString[i] == 'A' else myString[i].lower() for i in range(len(myString))]
    return ''.join(answer)
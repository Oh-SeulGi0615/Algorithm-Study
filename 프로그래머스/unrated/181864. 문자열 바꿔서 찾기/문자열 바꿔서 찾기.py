def solution(myString, pat):
    myString = ['B' if i == 'A' else 'A' for i in myString]
    string = ''.join(myString)

    if pat in string:
        return 1
    else:
        return 0
def solution(myString, pat):
    arr = list(myString)[::-1]
    b = list(pat)[::-1]
    
    for i in range(len(arr)-len(b)+1):
        if arr[i:i+len(b)] == b:
            return ''.join(arr[i:][::-1])
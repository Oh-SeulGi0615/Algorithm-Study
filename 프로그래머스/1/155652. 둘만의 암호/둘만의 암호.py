def solution(s, skip, index):
    answer = ''
    alphabet = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    for char in s:
        answer += alphabet[(alphabet.index(char) + index) % len(alphabet)]
    return answer
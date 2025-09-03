def solution(survey, choices):
    pattern = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    center = 4

    for i in range(len(survey)):
        if choices[i] < 4:
            pattern[survey[i][0]] += abs(choices[i] - center)
        elif choices[i] > 4:
            pattern[survey[i][1]] += abs(choices[i] - center)
    
    result = ''
    if pattern['R'] >= pattern['T']:
        result += 'R'
    else:
        result += 'T'
    
    if pattern['C'] >= pattern['F']:
        result += 'C'
    else:
        result += 'F'
    
    if pattern['J'] >= pattern['M']:
        result += 'J'
    else:
        result += 'M'
    
    if pattern['A'] >= pattern['N']:
        result += 'A'
    else:
        result += 'N'
    
    return result
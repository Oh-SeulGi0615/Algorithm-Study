import sys
input = sys.stdin.readline

for _ in range(int(input())):
    best_school = ''
    best_score = 0
    
    for _ in range(int(input())):
        school, score = map(str, input().split())
        if int(score) > best_score:
            best_score = int(score)
            best_school = school

    print(best_school)
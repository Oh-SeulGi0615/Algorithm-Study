def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    
    score = [0,0,0]
    for i in range(len(answers)):
        s1_idx = i % 5
        s2_idx = i % 8
        s3_idx = i % 10

        if answers[i] == s1[s1_idx]:
            score[0] += 1
        if answers[i] == s2[s2_idx]:
            score[1] += 1
        if answers[i] == s3[s3_idx]:
            score[2] += 1

    answer = [i+1 for i in range(len(score)) if score[i] == max(score)]
    answer.sort()
    return answer
function solution(array, height) {
    var answer = 0;
    for (const man of array) {
        if (man > height) {
            answer += 1
        }
    }
    return answer;
}
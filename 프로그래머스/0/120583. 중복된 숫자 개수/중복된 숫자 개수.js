function solution(array, n) {
    var answer = 0;
    for (const component of array) {
        if (component === n) {
            answer += 1
        }
    }
    
    return answer;
}
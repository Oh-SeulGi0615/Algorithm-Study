function solution(n) {
    let result = 0

    if (n >= 500000) {
        result = n * 0.8
    } else if (n >= 300000) {
        result = n * 0.9
    } else if (n >= 100000) {
        result = n * 0.95
    } else {
        result = n
    }

    return Math.trunc(result)
}
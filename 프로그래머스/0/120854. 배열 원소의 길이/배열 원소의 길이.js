function solution(n) {
    const arr = []
    for (const char of n) {
        len = char.length
        arr.push(len)
    }
    return arr
}
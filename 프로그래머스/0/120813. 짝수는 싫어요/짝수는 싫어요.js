function solution(n) {
    const arr = []
    for (let index = 1; index <= n; index++) {
        if (index%2 === 1) {
            arr.push(index)
        }   
    }
    return arr
}
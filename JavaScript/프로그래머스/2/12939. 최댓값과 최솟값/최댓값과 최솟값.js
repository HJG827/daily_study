function solution(s) {
    const numbers = s.split(' ').map(Number);
    const min = Math.min(...numbers)
    const max = Math.max(...numbers)
    
    var answer = `${min} ${max}`;
    return answer;
}
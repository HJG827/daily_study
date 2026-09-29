function solution(n) {
    var answer = '';
    const numbers = ["1", "2", "4"];
    
    while (n > 0) {
        n--;
        answer = numbers[n % 3] + answer;
        n = Math.floor(n / 3);
    }
    
    return answer;
}
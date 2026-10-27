function solution(n, k) {
    var answer = 0;
    
    function isPrime(num) {
        if (num < 2) return false;

        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i === 0) {
                return false;
            }
        }

        return true;
    }
    
    const numbers = n.toString(k)
        .split('0')
        .filter(num => num !== "")
        .map(Number);

    for (const number of numbers) {
        if (isPrime(number)) {
            answer++;
        }
    }
    
    return answer;
}
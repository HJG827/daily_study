function solution(numbers) {
    const set = new Set();
    const visited = Array(numbers.length).fill(false);
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
    
    function dfs(cur) {
        if (cur.length > 0) {
            set.add(Number(cur))
        }
        
        for (let i = 0; i < numbers.length; i++) {
            if (visited[i]) continue;
            
            visited[i] = true;
            dfs(cur + numbers[i]);
            visited[i] = false;
        }
    }
    
    dfs('')

    for (const number of set) {
        if (isPrime(number)) {
            answer++;
        }
    }
    
    return answer;
}
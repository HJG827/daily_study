function solution(numbers, target) {
    var answer = 0;
        
    function dfs(idx, cnt) {
        if (idx == numbers.length) {
            if (cnt == target) {
                answer++;
            }
            return
        }
        
        dfs(idx + 1, cnt + numbers[idx])
        dfs(idx + 1, cnt - numbers[idx])
    }
    
    dfs(0, 0)
    
    return answer;
}
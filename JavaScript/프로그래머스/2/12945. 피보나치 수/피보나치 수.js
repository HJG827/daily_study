function solution(n) {
    var dp = [0, 1];
    
    for (let i = 2; i <= n; i++) {
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1234567;
    }
    
    var answer = dp[n];
    return answer;
}
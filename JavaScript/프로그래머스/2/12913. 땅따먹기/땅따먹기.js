function solution(land) {
    let dp = [...land[0]];
    
    
    for (let i = 1; i < land.length; i++) {
        const next = Array(4).fill(0);
        
        next[0] = land[i][0] + Math.max(dp[1], dp[2], dp[3]);
        next[1] = land[i][1] + Math.max(dp[0], dp[2], dp[3]);
        next[2] = land[i][2] + Math.max(dp[0], dp[1], dp[3]);
        next[3] = land[i][3] + Math.max(dp[0], dp[1], dp[2]);
        
        dp = next;
    }

    return Math.max(...dp);
}
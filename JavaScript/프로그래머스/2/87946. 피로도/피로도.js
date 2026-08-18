function solution(k, dungeons) {
    let answer = 0;
    const visited = Array(dungeons.length).fill(false);
    
    function dfs(now_k, cnt) {
        answer = Math.max(answer, cnt);
        
        for (let i = 0; i < dungeons.length; i++) {
            if (
                visited[i] === false
                && now_k >= dungeons[i][0]
            ) {
                visited[i] = true;
                dfs(now_k - dungeons[i][1], cnt + 1);
                visited[i] = false;
            }
        }
    }
    
    dfs(k, 0)
    
    return answer;
}
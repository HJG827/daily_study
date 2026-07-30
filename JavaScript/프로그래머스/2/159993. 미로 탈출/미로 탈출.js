function solution(maps) {
    var answer = 0;
    const dr = [0, 1, 0, -1];
    const dc = [1, 0, -1, 0];
    
    function setLocation(maps) {
        let sr, sc;
        let lr, lc;
        let er, ec;
        for (let r = 0; r < maps.length; r++) {
            for (let c = 0; c < maps[r].length; c++) {
                if (maps[r][c] === "S") {
                    sr = r;
                    sc = c;
                }
                else if (maps[r][c] === "L") {
                    lr = r;
                    lc = c;
                }
                else if (maps[r][c] === "E") {
                    er = r;
                    ec = c;
                }
            }
        }
        
        return {sr, sc, lr, lc, er, ec}
    }
    
    function bfs(start_r, start_c, goal_r, goal_c) {
        const visited = Array.from({length:maps.length}, ()=>
            Array(maps[0].length).fill(-1)
            );
        
        const q = [];
        q.push([start_r, start_c]);
        visited[start_r][start_c] = 0;
        
        while (q.length > 0) {
            const [tr, tc] = q.shift();
            
            if (tr === goal_r && tc === goal_c) {
                return visited[tr][tc]
            }
            
            for (let d = 0; d < 4; d++) {
                const nr = tr + dr[d];
                const nc = tc + dc[d];
                
                if (0 <= nr && nr < maps.length
                && 0 <= nc && nc < maps[0].length
                && maps[nr][nc] !== "X"
                && visited[nr][nc] === -1
                ) {
                    visited[nr][nc] = visited[tr][tc] + 1;
                    q.push([nr, nc])
                }
            }
        }
        return -1
    }
    
    const {sr, sc, lr, lc, er, ec} = setLocation(maps);

    const dist1 = bfs(sr, sc, lr, lc);
    const dist2 = bfs(lr, lc, er, ec);
    
    if (dist1 !== -1 && dist2 !== -1) {
        answer = dist1 + dist2;
    }
    else {
        answer = -1;
        
    }
    return answer;
}
function solution(maps) {
    const dr = [1, 0, -1, 0];
    const dc = [0, 1, 0, -1];
    
    function bfs(sr, sc) {
        const q = [];
        let head = 0;
        
        q.push([0, 0, 1]);
        maps[sr][sc] = 0;
        
        
        while (head < q.length) {
            const [r, c, dist] = q[head];
            head++
            
            if (r === maps.length - 1 && c === maps[0].length - 1) {
                return dist
            }
            
            for (let d = 0; d < 4; d++) {
                const nr = r + dr[d]
                const nc = c + dc[d]
                
                if (
                    0 <= nr && nr < maps.length
                    && 0 <= nc && nc < maps[0].length
                    && maps[nr][nc] === 1
                ) {
                    q.push([nr, nc, dist + 1]);
                    maps[nr][nc] = 0;
                }
            }
        }
        
        return -1;
    }
    
    return bfs(0, 0)
}
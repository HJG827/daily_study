function solution(N, road, K) {
    var answer = 0;
    const dist = Array(N + 1).fill(Infinity);
    const adj = Array.from({length: N + 1}, () => []);
    
    road.forEach(([a, b, c]) => {
                 adj[a].push([c, b]);
                 adj[b].push([c, a]);
    })
    
    const pq = [];
    pq.push([0, 1]);
    
    dist[1] = 0;
    
    while (pq.length > 0) {
        pq.sort((a, b) => a[0] - b[0]);
        const [nowDist, node] = pq.shift();
        
        for (const [cost, nextNode] of adj[node]) {
            const nextDist = nowDist + cost;
            
            if (nextDist < dist[nextNode]) {
                dist[nextNode] = nextDist;
                pq.push([nextDist, nextNode])
            }
        }
    }
    
    
    for (let i = 1; i < N + 1; i++) {
        if (dist[i] <= K) {
            answer++;
        }
    }

    return answer;
}
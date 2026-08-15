function solution(x, y, n) {
    const q = [];
    let head = 0;
    
    const visited = new Set();
    
    q.push([x, 0]);
    visited.add(x);
    
    while (head < q.length) {
        const [num, cnt] = q[head++];
        
        if (num === y) {
            return cnt;
        }
        
        const nextNums = [num + n, num * 2, num * 3];
        
        for (const next of nextNums) {
            if (next <= y && !visited.has(next)) {
                visited.add(next);
                q.push([next, cnt + 1]);
            }
        }
    }
    
    return -1;
}
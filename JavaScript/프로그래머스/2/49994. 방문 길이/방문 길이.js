function solution(dirs) {
    var answer = 0;
    let r = 0;
    let c = 0;
    
    const visited = new Set();
    
    for (const dir of dirs) {
        let nr = r;
        let nc = c;
        
        if (dir === "U") {
            nr++;
        } else if (dir === "D") {
            nr--;
        } else if (dir === "R") {
            nc++;
        } else if (dir === "L") {
            nc--;
        }
        
        if (nr > 5 || nr < -5 || nc > 5 || nc < -5) {
            continue
        }
        
        const path = `${r}, ${c} -> ${nr}, ${nc}`
        const reversePath = `${nr}, ${nc} -> ${r}, ${c}`
        
        if (!visited.has(path)) {
            visited.add(path);
            visited.add(reversePath);
            answer++;
        }
        
        r = nr;
        c = nc;
    }
    
    
    return answer;
}
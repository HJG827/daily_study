function solution(n) {
    const triangle = [];

    for (let i = 0; i < n; i++) {
        const row = Array(i + 1).fill(0);
        triangle.push(row);
    }
    
    let r = -1;
    let c = 0;
    let num = 1;
    
    for (let len = n; len > 0; len -= 3) {
        
        for (let i = 0; i < len; i++) {
            triangle[++r][c] = num++;
        }
        
        for (let i = 0; i < len - 1; i++) {
            triangle[r][++c] = num++;
        }
        
        for (let i = 0; i < len - 2; i++) {
            triangle[--r][--c] = num++;
        }
    }
    
    return triangle.flat();
}
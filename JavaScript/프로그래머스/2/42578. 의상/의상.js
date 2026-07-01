function solution(clothes) {
    var answer = 1;
    
    const map = new Map();
    
    for (const [name, type] of clothes) {
        map.set(type, (map.get(type) || 0) + 1);
    }
    
    for (const cnt of map.values()) {
        answer *= (cnt + 1);
    }
    
    return answer - 1;
}
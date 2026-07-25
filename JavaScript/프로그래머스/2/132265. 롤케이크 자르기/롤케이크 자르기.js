function solution(topping) {
    var answer = 0;
    const leftmap = new Map();
    const rightmap = new Map();
    
    for (const top of topping) {
        rightmap.set(top, (rightmap.get(top) || 0) + 1);
    }
    
    for (let i = 0; i < topping.length; i++) {
        const now = topping[i];
        
        leftmap.set(now, (leftmap.get(now) || 0) + 1);
        
        rightmap.set(now, (rightmap.get(now) || 0) - 1);
        
        if (rightmap.get(now) === 0) {
            rightmap.delete(now);
        }
        
        if (leftmap.size === rightmap.size) {
            answer++;
        }   
    }
    
    return answer;
}
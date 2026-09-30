function solution(orders, course) {
    const menuMap = new Map();
    
    function combination(arr, start, picked, len) {
        if (picked.length === len) {
            menuMap.set(picked, (menuMap.get(picked) || 0) + 1);
            return;
        }
        
        for (let i = start; i < arr.length; i++) {
            combination(arr, i + 1, picked + arr[i], len);
        }
    }
    
    for (const order of orders) {
        const menu = order.split("").sort();
        
        for (const len of course) {
            combination(menu, 0, "", len);
        }
    }
        
    const answer = [];
    
    for (const len of course) {
        let maxCount = 0;
        
        for (const [menu, count] of menuMap) {
            if (menu.length === len) {
                maxCount = Math.max(maxCount, count)
            }
        }
        
        if (maxCount < 2) continue;
        
        for (const [menu, count] of menuMap) {
            if (menu.length === len && count === maxCount) {
                answer.push(menu);
            }
        }
    }
    
    answer.sort();
    return answer;
}
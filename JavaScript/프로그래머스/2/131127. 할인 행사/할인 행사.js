function solution(want, number, discount) {
    var answer = 0;
    let wantMap = new Map();
    let saleMap = new Map();
    
    for (let i = 0; i < want.length; i++) {
        const item = want[i];
        const cnt = number[i];
        wantMap.set(item, cnt);
    }
    
    for (let i = 0; i < 10; i++) {
        const item = discount[i];
        saleMap.set(item, (saleMap.get(item) || 0) + 1);
    }
    
    function getItem(wantMap, saleMap) {
        for (const [item, cnt] of wantMap) {
            if (saleMap.get(item) !== cnt) {
                return false;
            }
        }
        return true;
    }
    
    if (getItem(wantMap, saleMap)) {
        answer++;
    }
    
    for (let i = 10; i < discount.length; i++) {
        const outItem = discount[i - 10];
        const inItem = discount[i];
        
        saleMap.set(outItem, saleMap.get(outItem) - 1);
        if (saleMap.get(outItem) === 0) {
            saleMap.delete(outItem);
        }
        saleMap.set(inItem, (saleMap.get(inItem) || 0) + 1);
        
        if (getItem(wantMap, saleMap)) {
        answer++;
        }
    }
    
    return answer;
}
function solution(k, tangerine) {
    var answer = 0;
    
    const countMap = new Map();
    
    for (let size of tangerine) {
        countMap.set(size, (countMap.get(size) || 0) + 1);
    }
        
    const countList = [...countMap.values()];
    countList.sort((a, b) => b - a);
    
    for (let count of countList) {
        k -= count;
        answer++;
        
        if (k <= 0) {
            break;
        }
    }
    
    return answer;
}
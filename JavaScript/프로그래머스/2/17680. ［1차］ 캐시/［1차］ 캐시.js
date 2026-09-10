function solution(cacheSize, cities) {
    var answer = 0;
    const cache = [];
    
    if (cacheSize === 0) {
        return cities.length * 5;
    }
    
    for (const rawCity of cities) {
        const city = rawCity.toLowerCase();
        
        const idx = cache.indexOf(city);
        
        if (idx !== -1) {
            answer++;
            
            cache.splice(idx, 1);
            cache.push(city);
        } else {
            answer += 5;
            
            if (cache.length >= cacheSize) {
                cache.shift();
            }
            
            cache.push(city);
        }
    }
    
    
    return answer;
}
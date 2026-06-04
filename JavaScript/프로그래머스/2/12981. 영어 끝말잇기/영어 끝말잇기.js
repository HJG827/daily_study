function solution(n, words) {
    let answer = [0, 0];

    const used = new Set();
    used.add(words[0]);
    
    for (let i = 1; i < words.length; i++) {
        const prev = words[i - 1];
        const now = words[i];
        
        if (prev[prev.length - 1] != now[0]) {
            answer = [i % n + 1, Math.floor(i / n) + 1]
            break
        }
        else if (used.has(now)) {
            answer = [i % n + 1, Math.floor(i / n) + 1]
            break
        }
        
        used.add(now);
        
    }

    return answer;
}
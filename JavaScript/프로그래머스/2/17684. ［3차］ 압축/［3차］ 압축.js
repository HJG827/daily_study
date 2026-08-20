function solution(msg) {
    var answer = [];
    
    const dict = new Map();
    
    for (let i = 0; i < 26; i++) {
        const alphabet = String.fromCharCode(65 + i);
        dict.set(alphabet, i + 1);
    }
    
    let idx = 27;
    let i = 0;
    
    while (i < msg.length) {
        let w = msg[i];
        let j = i + 1;
        
        while (j <= msg.length && dict.has(w + msg[j])) {
            w += msg[j];
            j++;
        }
        
        answer.push(dict.get(w));
        
        if (j < msg.length) {
            dict.set(w + msg[j], idx);
            idx++;
        }
        
        i += w.length;
    }
    return answer;
}
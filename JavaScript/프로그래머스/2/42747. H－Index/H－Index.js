function solution(citations) {
    var answer = 0;
    
    citations.sort((a, b) => b - a);
     
    for (let i = 0; i < citations.length; i++) {
        const cnt = i + 1;
        
        if (citations[i] >= cnt) {
            answer = cnt;
        }
    }
    
    
    return answer;
}
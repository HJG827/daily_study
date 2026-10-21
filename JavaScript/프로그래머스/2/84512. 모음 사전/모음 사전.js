function solution(word) {
    var answer = 0;
    
    const vowels = {
        A: 0,
        E: 1,
        I: 2,
        O: 3,
        U: 4
    };
    
    const weight = [781, 156, 31, 6, 1];
    
    for (let i = 0; i < word.length; i++) {
        answer += vowels[word[i]] * weight[i] + 1;
    }
    
    return answer;
}
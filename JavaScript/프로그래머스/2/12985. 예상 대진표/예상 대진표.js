function solution(n,a,b)
{
    var answer = 0;

    while (true) {
        answer++;
        
        a = Math.trunc((a + 1) / 2);
        b = Math.trunc((b + 1) / 2);
        
        // console.log('answer:', answer, 'a:', a, 'b:', b)
        if (a === b) {
            break
        }
        
    }

    return answer;
}
function solution(order) {
    var answer = 0;
    let box = 1;
    const stack = [];
    
    for (const target of order) {
        
        while (box < target) {
            stack.push(box);
            box++;
        }
        
        if (box === target) {
            answer++;
            box++;            
        }
        
        else if (stack[stack.length - 1] === target) {
            stack.pop();
            answer++;
        }
        
        else break;
    }
    
    return answer;
}
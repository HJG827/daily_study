function solution(s){
    var answer = true;
    
    const stack = [];
    
    for (const ch of s) {
        if (ch == "(") {
            stack.push(ch)
        }
        else if (stack.length == 0) {
            answer = false;
            break
        }
        else {
            stack.pop();
        }
    }

    if (stack.length != 0) {
        answer = false;
    }
    return answer;
}
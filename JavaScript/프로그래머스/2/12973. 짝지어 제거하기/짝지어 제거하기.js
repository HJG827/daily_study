function solution(s)
{
    var answer = 0;

    var stack = [];
    let top = -1;
    for (let i = 0; i < s.length; i++) {
        if (stack.length == 0) {
            stack.push(s[i]);
            top++;
        }
        else {
            if (stack[top] == s[i]) {
                stack.pop();
                top--;
            }
            else {
                stack.push(s[i]);
                top++;
            }
        }
    }

    if (stack.length == 0) {
        answer = 1;
    }
    return answer;
}
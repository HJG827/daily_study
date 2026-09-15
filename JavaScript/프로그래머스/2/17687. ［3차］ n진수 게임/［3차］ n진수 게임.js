function solution(n, t, m, p) {
    var answer = '';
    var number = '_';
    
    let num = 0;

    while (number.length < t * m) {
        number += num.toString(n).toUpperCase();
        num++;
    }

    for (let i = p; answer.length < t; i += m) {
        answer += number[i];
    }

    return answer;
}
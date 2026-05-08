function solution(s) {
    var words = s.split(" ")
    var answer = words.map((word) => {
        return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
    })
    return answer.join(' ');
}